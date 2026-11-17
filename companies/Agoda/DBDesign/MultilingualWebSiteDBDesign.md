# System Design: Database Schema for a Multilingual Website

This is a common backend/database design interview question. The key challenge is designing a schema that supports multiple languages without duplicating the entire website's data.

For example, imagine an e-commerce website supporting:

- English (`en`)
- Hindi (`hi`)
- French (`fr`)
- German (`de`)

A product has common attributes such as price, SKU, inventory, and category, but its name and description vary by language.

I'd recommend a normalized schema with separate translation tables.

## 1. Understand the requirements

Before designing the schema, clarify:

1. Does the website support a fixed set of languages or dynamically configurable languages?
2. Which fields need translation?
3. Can a translation be missing for a particular language?
4. Should URLs and SEO metadata also be localized?
5. Can different languages have different content or only translated text?

For this design, assume:

- Languages are configurable.
- Product attributes are shared across languages.
- Product names, descriptions, and SEO metadata are translated.
- A missing translation falls back to the default language.
- Products have one canonical identity across all languages.

## 2. Database schema

[PHP internationalization - i18n mechanisms tutorial](https://images.openai.com/static-rsc-4/gUnqLChspn-sb_FMXBltOBwZLK4gupyX6II64kj-RzQNpr8LWb20_3eEiR1iiLMPG6uut-LXmOBSlR4eHNQDp691JnExRLKijMMDSX08dvRhAOMn-cnP3lFXZC_rBfWJgVO0jxIH0WiBLNAUaAh3zO--oUrJ7iJ-cbLWbzhC2GM?purpose=inline)

[lingohub.com](https://lingohub.com/blog/php-internationalization-i18n-mechanisms-tutorial?utm_source=chatgpt.com)

I'd create three primary tables.

### A. Languages

Stores supported languages.

```
CREATE TABLE languages (
    id BIGSERIAL PRIMARY KEY,
    language_code VARCHAR(10) UNIQUE NOT NULL,
    language_name VARCHAR(100) NOT NULL,
    is_default BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE
);
```

Example:

| id | language_code | language_name |
| -- | ------------- | ------------- |
| 1  | en            | English       |
| 2  | hi            | Hindi         |
| 3  | fr            | French        |
| 4  | de            | German        |

### B. Products

Stores language-independent product attributes.

```
CREATE TABLE products (
    id BIGSERIAL PRIMARY KEY,
    sku VARCHAR(100) UNIQUE NOT NULL,
    price DECIMAL(12,2) NOT NULL,
    inventory INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Example:

| id  | sku         | price | inventory |
| --- | ----------- | ----- | --------- |
| 101 | IPHONE-16   | 79999 | 50        |
| 102 | SAMSUNG-S24 | 74999 | 30        |

Notice that product name and description are not stored here.

### C. Product translations

Stores language-specific attributes.

```
CREATE TABLE product_translations (
    id BIGSERIAL PRIMARY KEY,
    product_id BIGINT REFERENCES products(id),
    language_id BIGINT REFERENCES languages(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    seo_title VARCHAR(255),
    seo_description TEXT,
    slug VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(product_id, language_id),
    UNIQUE(language_id, slug)
);
```

Example:

| product_id | language_id | name      | description              |
| ---------- | ----------- | --------- | ------------------------ |
| 101        | 1           | iPhone 16 | Latest Apple smartphone  |
| 101        | 2           | आईफोन 16  | नवीनतम Apple स्मार्टफोन  |
| 101        | 3           | iPhone 16 | Dernier smartphone Apple |

This gives us one product with multiple translations.

## 3. How to fetch a product in a requested language

Suppose the user requests a product in Hindi.

```
SELECT
    p.id,
    p.sku,
    p.price,
    p.inventory,
    COALESCE(pt.name, default_pt.name) AS name,
    COALESCE(pt.description, default_pt.description) AS description
FROM products p
JOIN languages default_lang
    ON default_lang.is_default = TRUE
LEFT JOIN product_translations pt
    ON pt.product_id = p.id
    AND pt.language_id = (
        SELECT id FROM languages
        WHERE language_code = 'hi'
    )
LEFT JOIN product_translations default_pt
    ON default_pt.product_id = p.id
    AND default_pt.language_id = default_lang.id
WHERE p.id = 101;
```

If the Hindi translation doesn't exist, the query returns the English translation.

For performance, I'd resolve the language ID once per request rather than execute a language lookup for every product.

## 4. Extending the schema to other website entities

The same approach works for categories, pages, articles, and navigation menus.

For example:

```
CREATE TABLE categories (
    id BIGSERIAL PRIMARY KEY,
    parent_id BIGINT REFERENCES categories(id),
    display_order INT DEFAULT 0
);

CREATE TABLE category_translations (
    id BIGSERIAL PRIMARY KEY,
    category_id BIGINT REFERENCES categories(id),
    language_id BIGINT REFERENCES languages(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    slug VARCHAR(255),
    UNIQUE(category_id, language_id),
    UNIQUE(language_id, slug)
);
```

For CMS pages:

```
CREATE TABLE pages (
    id BIGSERIAL PRIMARY KEY,
    page_type VARCHAR(50),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE page_translations (
    id BIGSERIAL PRIMARY KEY,
    page_id BIGINT REFERENCES pages(id),
    language_id BIGINT REFERENCES languages(id),
    title VARCHAR(255),
    content TEXT,
    slug VARCHAR(255),
    meta_title VARCHAR(255),
    meta_description TEXT,
    UNIQUE(page_id, language_id),
    UNIQUE(language_id, slug)
);
```

This allows each entity to have its own translation table, which keeps the schema strongly typed and easy to query.

## 5. Alternative approaches

Interviewers often ask why we chose separate translation tables instead of other approaches.

| Approach                    | Example                            | Advantages                      | Disadvantages                    |
| --------------------------- | ---------------------------------- | ------------------------------- | -------------------------------- |
| Separate columns            | `name_en`, `name_hi`               | Simple for fixed languages      | Schema changes for new languages |
| JSONB column                | `name = {"en":"Phone","hi":"फोन"}` | Flexible, fewer tables          | Harder constraints and indexing  |
| Separate translation tables | `product_translations`             | Normalized, scalable, queryable | Requires joins                   |

### Option 1: Separate language columns

```
CREATE TABLE products (
    id BIGINT PRIMARY KEY,
    name_en VARCHAR(255),
    name_hi VARCHAR(255),
    name_fr VARCHAR(255)
);
```

I would avoid this because adding a language requires a schema migration.

### Option 2: JSONB

PostgreSQL supports JSONB:

```
CREATE TABLE products (
    id BIGSERIAL PRIMARY KEY,
    sku VARCHAR(100),
    price DECIMAL(12,2),
    name JSONB,
    description JSONB
);
```

Example:

```
{
  "en": "Smartphone",
  "hi": "स्मार्टफोन",
  "fr": "Téléphone intelligent"
}
```

This is reasonable when:

- Translated attributes are relatively simple.
- The number of languages changes frequently.
- Most queries fetch the entire translation object.
- You don't need strong relational constraints for each translation.

However, filtering, uniqueness constraints, and indexing individual translated fields can become more complicated.

### My choice



Recommended

&#x20;Separate translation tables for a typical multilingual e-commerce or CMS application.



They provide a good balance between normalization, queryability, and extensibility.

## 6. Important senior-level considerations

### A. Language fallback hierarchy

Imagine the requested language is `fr-CA` (Canadian French).

You may want this fallback sequence:

```
fr-CA → fr → en
```

Store language tags using BCP 47 conventions where appropriate.

The application should resolve the fallback chain and choose the first available translation.

### B. Localized URLs and SEO

Example:

```
/en/products/iphone-16
/hi/products/iphone-16
/fr/products/iphone-16
```

Store slugs in the translation table and enforce:

```
UNIQUE(language_id, slug)
```

Also consider:

- `hreflang` metadata.
- Canonical URLs.
- Localized meta titles and descriptions.
- Redirects when a slug changes.

### C. Search

Searching for products in different languages requires language-aware tokenization and stemming.

For PostgreSQL, you can use:

- Full-text search configurations.
- Language-specific search vectors.
- Trigram indexes for fuzzy matching.

For larger search requirements, consider Elasticsearch or OpenSearch with language-specific analyzers.

### D. Caching

Cache localized content using a key such as:

```
product:101:en
product:101:hi
product:101:fr
```

Be careful to invalidate all affected language variants when shared product data changes.

### E. Missing translations

Do not assume all translations are available.

Possible approaches:

- Fall back to the default language.
- Mark a translation as draft or unpublished.
- Hide pages whose requested translation is unavailable.
- Track translation completeness.

## 7. Important database indexes

For PostgreSQL:

```
CREATE INDEX idx_product_translations_product_language
ON product_translations(product_id, language_id);

CREATE UNIQUE INDEX idx_product_translation_slug
ON product_translations(language_id, slug);

CREATE INDEX idx_products_sku
ON products(sku);
```

The unique constraint on `(product_id, language_id)` already creates an index in PostgreSQL, so you generally wouldn't create the first index again.

## 8. Interview follow-up questions

These are the questions I'd prepare for at senior level:

1. What if 100 million products support 20 languages? How would you optimize queries?
2. How would you handle translations that are updated independently?
3. How would you migrate from a single-language website to a multilingual one without downtime?
4. How would you support language fallback such as `fr-CA → fr → en`?
5. How would you design multilingual search?
6. How would you handle concurrent updates to translations?
7. Would you use PostgreSQL JSONB or separate tables at scale?
8. How would you ensure a user never sees a partially published translation?

My recommendation for the interview: Lead with the normalized translation-table approach, explain why product data and translated data are separate, demonstrate the fallback query, and then discuss JSONB as an alternative.

The most important design principle is: store language-independent attributes once, and store language-dependent attributes separately for each supported language.

1. What if 100 million products support 20 languages? How would you optimize queries?
For 100 million products supporting 20 languages, the challenge is no longer just schema normalization. It becomes a large-scale data retrieval, indexing, caching, partitioning, and query optimization problem.

I'd approach this as a senior backend engineer and distinguish between the database storage strategy and the read-serving strategy.

## 1. Understand the scale

Assume:

- 100 million products.
- 20 supported languages.
- Every product has a translation in every language.
- Approximately 2 billion translation records.

# 100M

Products

# 20

Languages

# 2B

Translation records

# 20×

Translation rows per product

The original schema is logically sound, but querying billions of translation rows requires careful optimization.

## 2. Optimize the database schema

I would keep product attributes and translations separate.

```
CREATE TABLE products (
    id BIGINT PRIMARY KEY,
    sku VARCHAR(100) NOT NULL,
    price NUMERIC(12,2),
    inventory INT,
    created_at TIMESTAMP
);

CREATE TABLE product_translations (
    product_id BIGINT NOT NULL,
    language_code VARCHAR(10) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    slug VARCHAR(255),
    updated_at TIMESTAMP,

    PRIMARY KEY (product_id, language_code)
);
```

Notice that I use `language_code` directly instead of joining the `languages` table for every product read.

Why?

- Avoids an unnecessary join.
- Simplifies query execution.
- Makes language filtering straightforward.
- Keeps the language identifier compact.

The languages table can still exist for language configuration and validation.

## 3. Create the right indexes

This is one of the most important optimization decisions.

### Index 1: Primary key for product and language

```
PRIMARY KEY (product_id, language_code)
```

This supports:

```
SELECT name, description
FROM product_translations
WHERE product_id = 10001
AND language_code = 'hi';
```

This is efficient for fetching one product in one language.

### Index 2: Reverse index for language-based queries

```
CREATE INDEX idx_translation_language_product
ON product_translations(language_code, product_id);
```

This supports queries such as:

```
SELECT product_id, name
FROM product_translations
WHERE language_code = 'hi'
ORDER BY product_id
LIMIT 100;
```

The order of columns in a composite index matters.

- `(product_id, language_code)` is ideal for product-first lookup.
- `(language_code, product_id)` is useful for language-first lookup.

Don't create both automatically. Create indexes based on actual query patterns and execution plans.

## 4. Partition the translation table

At 2 billion rows, I would evaluate partitioning.

One possible strategy is hash partitioning by `product_id`.

```
CREATE TABLE product_translations (
    product_id BIGINT NOT NULL,
    language_code VARCHAR(10) NOT NULL,
    name VARCHAR(255),
    description TEXT,
    PRIMARY KEY (product_id, language_code)
) PARTITION BY HASH (product_id);
```

Create 64 partitions:

```
CREATE TABLE product_translations_0
PARTITION OF product_translations
FOR VALUES WITH (MODULUS 64, REMAINDER 0);

CREATE TABLE product_translations_1
PARTITION OF product_translations
FOR VALUES WITH (MODULUS 64, REMAINDER 1);
```

Repeat for the remaining partitions.

Why hash partitioning by product ID?

A query for one product and one language includes the product ID, so PostgreSQL can prune to a single partition.

For example:

```
SELECT *
FROM product_translations
WHERE product_id = 10001
AND language_code = 'hi';
```

However, if the dominant query is fetching all products in a particular language, hash partitioning by product ID will not prune partitions for that query.

This is an important trade-off.

Also, partitioning does not automatically distribute data across multiple database servers. PostgreSQL partitioning is primarily a table-management and query-pruning mechanism within a database cluster.

## 5. Optimize the actual product listing query

Suppose the website displays products in Hindi.

A naive query might join all translations and products, then filter and sort.

Instead, filter and paginate products first, then retrieve the relevant translations.

```
SELECT
    p.id,
    p.sku,
    p.price,
    pt.name,
    pt.description
FROM products p
JOIN product_translations pt
    ON pt.product_id = p.id
    AND pt.language_code = 'hi'
WHERE p.id > 10000
ORDER BY p.id
LIMIT 50;
```

This is a simple example of keyset pagination.

For a more complex catalog query, first identify the 50 product IDs using indexed filters and sorting, then join their translations.

Avoid:

```
LIMIT 50 OFFSET 1000000;
```

Large offsets become increasingly expensive because the database still needs to walk past the preceding rows.

Use keyset pagination:

```
WHERE p.id > :last_seen_id
ORDER BY p.id
LIMIT 50;
```

For sorting by price, use a composite cursor such as `(price, id)`.

## 6. Introduce caching

At this scale, I would not send every product read directly to PostgreSQL.

Use a layered caching strategy.

Client / CDN

Localized pages and public product content

Application cache – Redis

Frequently accessed product translations

Database read replicas

Read-heavy product and translation queries

Primary PostgreSQL

Writes and authoritative data

Example Redis key:

```
product:10001:hi
product:10001:en
product:10001:fr
```

Cache the product's translated content independently from frequently changing inventory or price, if those have different update patterns.

For example:

```
product-content:10001:hi
product-price:10001
product-inventory:10001
```

This avoids invalidating translated descriptions every time inventory changes.

## 7. Use read replicas

A typical deployment:

```
                Application
                     |
               Database Router
                /          \
               /            \
          Write path      Read path
              |               |
         Primary DB       Read Replica 1
                              |
                          Read Replica 2
                              |
                          Read Replica 3
```

- All writes go to the primary.
- Product listing and translation reads go to replicas.
- Redis handles frequently requested content.
- Read replicas can be scaled independently to handle read traffic.

One caveat: replicas are eventually consistent with the primary. If a user updates a translation and immediately requests it, route that read to the primary or use a read-your-writes strategy.

## 8. Consider language-based sharding

At a much larger scale, you could consider distributing translation data across database shards.

For example:

```
Translation database cluster

Shard 1: English, Hindi, French, German
Shard 2: Spanish, Italian, Portuguese, Dutch
Shard 3: Japanese, Chinese, Korean, Thai
Shard 4: Other languages
```

But I would be cautious about this approach.

A product page request for one language can be routed to one shard, but:

- Products with multiple language translations span shards.
- Cross-language queries become expensive.
- Product updates may require coordination across shards.
- Rebalancing becomes more complicated.

An alternative is sharding by `product_id`, keeping all 20 language translations for a product together.

My preference: Shard by product ID if product-centric reads dominate. Consider language-based distribution only if language-specific workloads are sufficiently independent and justify the operational complexity.

## 9. Separate search from transactional database queries

One important distinction: product browsing often involves searching by name, filtering, ranking, and sorting.

For example:

- Search for "smartphone" in Hindi.
- Filter by category.
- Sort by popularity.
- Filter by price range.

I would not use PostgreSQL as the only search engine at this scale.

Use OpenSearch or Elasticsearch with language-specific analyzers.

Example search document:

```
{
  "product_id": 10001,
  "price": 79999,
  "translations": {
    "en": {
      "name": "Smartphone",
      "description": "Latest smartphone"
    },
    "hi": {
      "name": "स्मार्टफोन",
      "description": "नवीनतम स्मार्टफोन"
    }
  }
}
```

Or maintain separate language-specific indexes when the search workloads require independent scaling.

The database remains the source of truth. Changes are propagated to search through an event-driven indexing pipeline.

## 10. My recommended architecture

Web / Mobile Clients

API Gateway + Product Service

Language resolution, authorization, pagination

Redis

Localized content cache

OpenSearch

Multilingual search

PostgreSQL

Products + translations, partitioned and indexed

Primary

Read replicas

Hash partitions

Kafka / CDC pipeline

Search indexing and cache invalidation

## 11. What I would say in the interview

"I would retain a normalized product and translation schema, with a composite primary key on product ID and language code. At two billion translation records, I'd evaluate hash partitioning by product ID to optimize product-centric lookups and use appropriate composite indexes based on query patterns.

For read scalability, I'd introduce Redis caching, read replicas, and keyset pagination. I'd keep multilingual search outside the transactional database using OpenSearch with language-specific analyzers, synchronizing changes through an event-driven pipeline.

I would avoid introducing sharding immediately. First, I'd benchmark the workload, inspect query plans, measure cache hit ratios, and identify whether the bottleneck is CPU, I/O, indexing, or network traffic. I'd introduce distributed sharding only when a single database cluster can no longer meet the throughput or storage requirements."

## 12. Follow-up questions worth preparing

Choose a senior-level follow-up to explore

How would you handle a product update across all 20 languages atomically?

What if 80% of traffic comes from English and 20% from the other languages?

Would you partition by product ID or language code, and why?

How would you migrate from PostgreSQL to a sharded database without downtime?

How would you ensure Redis and OpenSearch remain consistent with PostgreSQL?

Explore answer

One key interview insight: Two billion rows alone do not automatically require sharding. The right decision depends on query patterns, data size, write rate, read/write ratio, latency targets, and the capacity of the database infrastructure.

How would you handle a product update across all 20 languages atomically? Explain the solution with architecture, trade-offs, and interview-level details.
# Handling Product Updates Across 20 Languages Atomically

For this problem, I would use a database transaction combined with an event-driven architecture using the transactional outbox pattern.

The most important distinction to explain in the interview is:

- Database atomicity: All 20 language translations must be updated together, or none should be updated.
- System-wide consistency: Redis, OpenSearch, and other downstream systems must eventually reflect the committed database update.

I would guarantee the first synchronously and achieve the second asynchronously.

## 1. Requirements and assumptions

Suppose product `10001` has translations in 20 languages.

An administrator updates:

- Product name in all 20 languages.
- Product description in all 20 languages.
- SEO title and description.
- Product metadata such as price or category.

Requirements:

1. Either all 20 translations are updated or none are.
2. Concurrent updates must not overwrite each other silently.
3. Search indexes and caches must be updated.
4. Failed downstream processing must be retryable.
5. Consumers must not publish stale data over newer data.

I would use PostgreSQL as the source of truth.

## 2. Database schema

We already have two core tables.

```
CREATE TABLE products (
    id BIGINT PRIMARY KEY,
    sku VARCHAR(100) UNIQUE NOT NULL,
    price NUMERIC(12,2),
    version BIGINT NOT NULL DEFAULT 1,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_translations (
    product_id BIGINT NOT NULL,
    language_code VARCHAR(10) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    seo_title VARCHAR(255),
    version BIGINT NOT NULL DEFAULT 1,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (product_id, language_code),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

I would also introduce an outbox table.

```
CREATE TABLE outbox_events (
    event_id UUID PRIMARY KEY,
    aggregate_id BIGINT NOT NULL,
    aggregate_version BIGINT NOT NULL,
    event_type VARCHAR(100) NOT NULL,
    payload JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMP,

    UNIQUE(aggregate_id, aggregate_version, event_type)
);
```

The outbox table stores events in the same transaction as the product update.

This is important because updating PostgreSQL and publishing to Kafka directly are two independent operations.

## 3. Architecture

Admin / Product Management API

Receives all 20 translations in one request

Product Service

Validates languages, fields, and product version

Single ACID transaction

PostgreSQL

Products

20 translations

Transactional Outbox Event

CDC / Outbox Publisher

Publishes committed events to Kafka

Kafka – ProductUpdated topic

Partition key: product_id

Redis

Cache invalidation

OpenSearch

Search indexing

Other services

Catalog consumers

The key architectural decision is that PostgreSQL is responsible for atomicity. Kafka is responsible for distributing the committed change to downstream systems.

## 4. How the atomic database update works

Suppose the API receives:

```
{
  "product_id": 10001,
  "expected_version": 5,
  "translations": [
    {
      "language_code": "en",
      "name": "Smartphone",
      "description": "Latest smartphone"
    },
    {
      "language_code": "hi",
      "name": "स्मार्टफोन",
      "description": "नवीनतम स्मार्टफोन"
    },
    {
      "language_code": "fr",
      "name": "Téléphone",
      "description": "Dernier smartphone"
    }
  ]
}
```

The real request contains all 20 translations. This abbreviated example shows three.

I would execute the following operations inside one database transaction.

Step 1: Start transaction and lock product

```
BEGIN;

SELECT id, version
FROM products
WHERE id = 10001
FOR UPDATE;
```

The row lock prevents another transaction from simultaneously modifying this product.

Check that the current version is equal to `expected_version`.

If it is not, return a conflict response instead of silently overwriting another administrator's changes.

Step 2: Validate translations

Before updating:

- Verify all 20 required languages are present.
- Reject duplicate language codes.
- Reject unsupported language codes.
- Validate required fields and content lengths.
- Check whether the product is eligible for publication.

For example, if `fr` is missing, reject the request if the business rule requires all 20 translations.

Step 3: Update all translations

Use a bulk upsert:

```
INSERT INTO product_translations (
    product_id,
    language_code,
    name,
    description,
    version,
    updated_at
)
VALUES
    (10001, 'en', 'Smartphone', 'Latest smartphone', 6, NOW()),
    (10001, 'hi', 'स्मार्टफोन', 'नवीनतम स्मार्टफोन', 6, NOW()),
    (10001, 'fr', 'Téléphone', 'Dernier smartphone', 6, NOW())
    -- Remaining 17 languages
ON CONFLICT (product_id, language_code)
DO UPDATE SET
    name = EXCLUDED.name,
    description = EXCLUDED.description,
    version = EXCLUDED.version,
    updated_at = NOW();
```

Step 4: Increment product version

```
UPDATE products
SET version = version + 1,
    updated_at = NOW()
WHERE id = 10001;
```

Step 5: Insert outbox event

```
INSERT INTO outbox_events (
    event_id,
    aggregate_id,
    aggregate_version,
    event_type,
    payload
)
VALUES (
    gen_random_uuid(),
    10001,
    6,
    'ProductUpdated',
    '{"product_id": 10001, "version": 6}'
);
```

Step 6: Commit

```
COMMIT;
```



Atomic guarantee

&#x20;If any operation fails before commit, PostgreSQL rolls back the entire transaction, including all translation changes and the outbox event.



This is exactly what we need: no partially updated product across the 20 languages.

Important: The database transaction does not include Kafka, Redis, or OpenSearch. Those systems are updated after commit.

## 5. Why the transactional outbox pattern?

Consider this naive implementation:

```
update_product_in_database()publish_event_to_kafka()
```

There are two dangerous failure scenarios.

| Failure                                       | Result                                                           |
| --------------------------------------------- | ---------------------------------------------------------------- |
| Database update succeeds, Kafka publish fails | Database is updated, but downstream systems never learn about it |
| Kafka publish succeeds, database update fails | Consumers receive an event for a change that never committed     |

This is called the dual-write problem.

The transactional outbox solves it:

```
PostgreSQL transaction
    |
    +-- Update product
    |
    +-- Update 20 translations
    |
    +-- Insert outbox event
    |
    +-- COMMIT
             |
             v
       CDC / Publisher
             |
             v
           Kafka
```

A CDC tool such as Debezium can capture committed outbox inserts from PostgreSQL's write-ahead log and publish them to Kafka.

Alternatively, a background publisher can poll unpublished outbox rows.

I would generally prefer CDC for a high-throughput system because it avoids repeatedly polling the table, although it introduces CDC infrastructure and operational complexity.

### What if the publisher crashes?

Suppose the publisher sends an event to Kafka but crashes before marking it as published.

It may send the same event again after restarting.

That is acceptable if downstream consumers are idempotent.

Use `event_id` as the idempotency key.

The important guarantee is:

- No committed database update is missing its corresponding outbox record.
- Event publication is at least once, not necessarily exactly once.
- Consumers must handle duplicates.

## 6. How to update Redis and OpenSearch safely

After Kafka receives `ProductUpdated`, independent consumers process it.

### A. Redis cache invalidation

Suppose the cache contains:

```
product:10001:en
product:10001:hi
product:10001:fr
...
product:10001:de
```

The cache consumer can invalidate all 20 language variants.

```
def handle_product_updated(event):    product_id = event["product_id"]    keys = [        f"product:{product_id}:{language}"        for language in SUPPORTED_LANGUAGES    ]    redis.delete(*keys)
```

The next request loads the latest data from PostgreSQL and repopulates the cache.

A more robust approach: versioned cache keys

```
product:10001:en:v6
product:10001:hi:v6
product:10001:fr:v6
```

The application maintains or reads the current product version and requests the matching cache version.

This prevents an older in-flight request from repopulating an obsolete cache entry after a newer update.

However, versioned caching requires careful handling of the current-version pointer and TTLs. For a simpler implementation, invalidation plus short TTLs may be sufficient.

### B. OpenSearch indexing

Suppose OpenSearch maintains one document per product containing all language variants.

```
{
  "product_id": 10001,
  "version": 6,
  "translations": {
    "en": {
      "name": "Smartphone"
    },
    "hi": {
      "name": "स्मार्टफोन"
    },
    "fr": {
      "name": "Téléphone"
    }
  }
}
```

When a product update arrives:

1. Consumer reads the event.
2. Fetches the latest product and all translations.
3. Builds a complete search document.
4. Replaces the existing document in OpenSearch.
5. Records successful processing.

I prefer replacing the complete document rather than independently updating 20 language fields. It avoids exposing a mixture of old and new translations in the search document.

Important: OpenSearch updates are not part of the PostgreSQL transaction. Search can temporarily show the previous version.

For stronger protection against stale updates, use product versions:

```
Incoming event version = 6
Current indexed version = 7

Ignore event version 6.
```

You can use OpenSearch's external versioning or implement a version check in the indexing workflow. This prevents an older event from overwriting a newer indexed document.

## 7. Handling concurrent updates

This is an important senior-level discussion.

Imagine two administrators update the same product:

```
Admin A reads product version 5
Admin B reads product version 5

Admin A updates English and Hindi
Admin B updates French and German
```

Without concurrency control, one update could overwrite the other.

I would use optimistic concurrency control with a version field.

Admin A:

```
expected_version = 5
```

Admin B:

```
expected_version = 5
```

Admin A commits first:

```
product version = 6
```

Admin B attempts to update:

```
expected_version = 5
actual_version = 6
```



Conflict

&#x20;Admin B receives HTTP `409 Conflict`.



The administrator can reload the latest product and retry.

For the all-20-language update requirement, I would treat all 20 translations as one logical aggregate. That means a single product version is incremented for the entire translation set.

If the business allows independent language editing, we could instead maintain per-translation versions, but then the atomicity requirement needs to be clarified.

## 8. Handling failures and retries

| Scenario                                    | Expected behavior                             |
| ------------------------------------------- | --------------------------------------------- |
| Translation validation fails                | Reject request; no database changes           |
| One translation update fails                | Roll back entire transaction                  |
| PostgreSQL crashes before commit            | Transaction rolls back during recovery        |
| PostgreSQL commits but Kafka is unavailable | Outbox retains event for later publication    |
| CDC publisher crashes                       | Resume from WAL position; duplicates possible |
| Redis is unavailable                        | Retry invalidation; TTL provides fallback     |
| OpenSearch is unavailable                   | Consumer retries; lag increases               |
| Consumer processes event twice              | Idempotency check                             |
| Old event arrives after new event           | Reject based on product version               |

A useful operational mechanism is a dead-letter topic for events that repeatedly fail processing, with alerting and a controlled replay process.

One caveat: moving an event to a DLQ should not silently mark the product as fully synchronized. Track the downstream indexing or cache-invalidation status separately if that matters to operations.

## 9. A subtle question: What does "atomic across all 20 languages" mean to website users?

This is where I would distinguish two consistency requirements.

Requirement A: Database atomicity

A database query cannot see 10 new translations and 10 old translations from the same transaction. PostgreSQL MVCC ensures readers see a consistent committed snapshot.

Requirement B: Global atomic visibility

Suppose Redis and OpenSearch are updated asynchronously.

For a short period:

```
PostgreSQL: Version 6
Redis:      Version 5
OpenSearch: Version 5
```

Therefore, the whole website is not globally atomic.

If the interviewer requires users never to see mixed versions across language variants, I would introduce a publication/version mechanism.

For example:

```
Product 10001

Version 5: Published
Version 6: Being prepared
```

The system prepares all translations and search documents for version 6, then atomically switches a product's published-version pointer from 5 to 6.

The application only serves the currently published version.

This is similar to a blue-green deployment for product content.

There is an important distinction, though: a single PostgreSQL pointer switch cannot atomically switch Redis and OpenSearch at the same instant. If strict cross-system consistency is required, reads must be gated by the authoritative published version, or served from a single versioned read model. Otherwise, eventual consistency is the realistic guarantee.

## 10. Alternative: Version-based publication

For a catalog where content correctness is more important than immediate visibility, I would consider a two-phase publication workflow.

Instead of overwriting the currently published translations immediately:

Phase 1: Prepare

Store the new translations under version 6.

```
product_id | language | version | status
10001      | en       | 5       | PUBLISHED
10001      | en       | 6       | DRAFT
10001      | hi       | 5       | PUBLISHED
10001      | hi       | 6       | DRAFT
...
```

Validate all 20 translations and prepare the new search document.

Phase 2: Publish

Once all required translations are ready, atomically switch the product's published version:

```
UPDATE products
SET published_version = 6
WHERE id = 10001;
```

The application only serves translations matching `published_version`.

This provides a useful guarantee: a user sees either the complete previous version or the complete new version, never a partially published translation set.

However, it introduces:

- More storage because multiple versions are retained.
- More complex queries.
- A publication workflow.
- Cleanup of obsolete versions.
- Additional coordination with search and caching.

I would use this only when strict publication consistency is a real business requirement, not by default.

## 11. Trade-offs between approaches

| Approach                      | Atomicity                                     | Complexity | When to use                         |
| ----------------------------- | --------------------------------------------- | ---------- | ----------------------------------- |
| Single PostgreSQL transaction | All DB changes atomic                         | Low        | Default solution                    |
| Transaction + outbox          | DB atomicity, downstream eventual consistency | Medium     | Recommended production architecture |
| Version-based publication     | Complete content version visibility           | High       | Strict publishing requirements      |
| Distributed transaction / 2PC | Coordinates multiple systems                  | Very high  | Rarely justified for this use case  |

For 20 translations belonging to one product, a PostgreSQL transaction is inexpensive. I would not introduce distributed transactions merely to update these 20 rows.

## 12. Testing and observability

I'd add tests for:

- All 20 translations update successfully.
- One invalid translation causes complete rollback.
- Missing language causes validation failure.
- Two concurrent updates result in one successful update and one version conflict.
- Outbox events are eventually published after a Kafka outage.
- Duplicate events do not cause duplicate downstream effects.
- An older event cannot overwrite a newer OpenSearch document.
- Cache invalidation failure is retried.

Metrics I'd monitor:

| Metric                             | Why                                    |
| ---------------------------------- | -------------------------------------- |
| Product update transaction latency | Database performance                   |
| Transaction rollback rate          | Validation or database failures        |
| Outbox publishing lag              | Database-to-Kafka delay                |
| Consumer lag                       | Downstream processing delay            |
| Search indexing lag                | Search freshness                       |
| Cache invalidation failures        | Stale cache risk                       |
| Version mismatch count             | Out-of-order processing or concurrency |

## 13. My recommended interview answer

If I had to explain this in 2–3 minutes, I'd say:

"I'd treat a product and its 20 translations as a single logical aggregate. PostgreSQL would be the source of truth. When an update arrives, I'd validate all 20 translations and update them inside one ACID transaction. I'd use a product-level version number and optimistic concurrency control to prevent concurrent administrators from overwriting each other's changes.

In the same transaction, I'd insert a ProductUpdated event into an outbox table. A CDC mechanism such as Debezium would publish committed outbox events to Kafka. This solves the dual-write problem between the database and Kafka.

Redis and OpenSearch would consume these events independently. Redis would invalidate the 20 language-specific cache entries, while OpenSearch would replace the complete multilingual product document. I'd include the product version in events and downstream documents to prevent stale events from overwriting newer data.

The database update is atomic, while downstream systems are eventually consistent. If the business requires all languages to become visible together, I'd introduce version-based publication: prepare all translations and search data first, then atomically switch the published product version."

## 14. One important interview follow-up

Suppose PostgreSQL commits version 6, Kafka receives the event, but the OpenSearch consumer crashes halfway through indexing. Meanwhile, version 7 is committed. How do you ensure version 6 doesn't overwrite version 7 when the consumer recovers?

Retry version 6 until indexing succeeds, then process version 7.

Use product versions and reject any event older than the indexed version.

Lock the product row in PostgreSQL until OpenSearch indexing finishes.

Use a distributed transaction between PostgreSQL and OpenSearch.

Explain answer

This is a particularly good senior-level follow-up because it tests event ordering, idempotency, eventual consistency, and failure recovery together.