Spring Bean lifecycle methods
public void init()
public void destroy()

Spring IOC container:
1. maintains object lifecycle

3 kinds of DI : constructor, setter and field

Stereotype annotation
@Component @Service @Controller/@RestController @Repository

Spring core related annotation
@Configuration : class can be used by Spring IOC as a source of Bean definition
@ComponentScan : @ComponentScan("packageName") spring will create beans from components from this package
@Bean @Autowired @Primary @Qualifier @Lazy @Value @PropertySource @ConfigurationProperties @Profile @Scope

spring can't inject multiple beans from a single interface implementation. use either @Primary or @Qualifier with
@Autowired to tell spring IOC to which one to use

@Lazy will create the bean on demand. lazy loading
@Value will fetch value by key from config file application.properties
@PropertySource will read config from custom property file. such as custom.properties
@ConfigurationProperties will map custom.properties values to DTO
@Profile will load the properties of active profile

@RestControllerAdvice and @ExceptionHandler annotation handles thrown exceptions by Controller

Spring data JPA annotation
@Entity @Table @Transactional @Data @Id @Column @OneToOne @OneToMany @ManyToOne @ManyToMany @JoinColumn

Security annotation
@CrossOrigin @Secured @PreAuthorize @PermitAll

Caching annotation
@EnableCaching @Cacheable @CachePut @CacheEvict

Aspect oriented annotation
by default AOP is not enabled in spring
@Aspect @EnableAspectJAutoProxy @Pointcut @AfterRunning @AfterThrowing @Around @Before("execution(public void show())")