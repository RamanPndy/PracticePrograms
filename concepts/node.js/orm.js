// sequealize-cli helps in creating migrations

//To create an empty project you will need to execute init command
// npx sequelize-cli init - This will create following folders
// config, contains config file, which tells CLI how to connect with database
// models, contains all models for your project
// migrations, contains all migration files
// seeders, contains all seed files

// Creating model
// npx sequelize-cli model:generate --name User --attributes firstName:string,lastName:string,email:string

// Migration skeleton
module.exports = {
    up: (queryInterface, Sequelize) => {
      // logic for transforming into the new state
    },
    down: (queryInterface, Sequelize) => {
      // logic for reverting the changes
    },
  };

module.exports = {
    up: (queryInterface, Sequelize) => {
        return queryInterface.createTable('Person', {
        name: Sequelize.DataTypes.STRING,
        isBetaMember: {
            type: Sequelize.DataTypes.BOOLEAN,
            defaultValue: false,
            allowNull: false,
        },
        });
    },
    down: (queryInterface, Sequelize) => {
        return queryInterface.dropTable('Person');
    },
};

// create table
module.exports = {
    up: (queryInterface, Sequelize) => {
      return queryInterface.createTable('Person', {
        name: Sequelize.DataTypes.STRING,
        isBetaMember: {
          type: Sequelize.DataTypes.BOOLEAN,
          defaultValue: false,
          allowNull: false,
        },
        userId: {
          type: Sequelize.DataTypes.INTEGER,
          references: {
            model: {
              tableName: 'users',
              schema: 'schema',
            },
            key: 'id',
          },
          allowNull: false,
        },
      });
    },
    down: (queryInterface, Sequelize) => {
      return queryInterface.dropTable('Person');
    },
  };

// automatically managed transaction
module.exports = {
    up: (queryInterface, Sequelize) => {
      return queryInterface.sequelize.transaction(t => {
        return Promise.all([
          queryInterface.addColumn(
            'Person',
            'petName',
            {
              type: Sequelize.DataTypes.STRING,
            },
            { transaction: t },
          ),
          queryInterface.addColumn(
            'Person',
            'favoriteColor',
            {
              type: Sequelize.DataTypes.STRING,
            },
            { transaction: t },
          ),
        ]);
      });
    },
    down: (queryInterface, Sequelize) => {
      return queryInterface.sequelize.transaction(t => {
        return Promise.all([
          queryInterface.removeColumn('Person', 'petName', { transaction: t }),
          queryInterface.removeColumn('Person', 'favoriteColor', {
            transaction: t,
          }),
        ]);
      });
    },
  };

// manually managed transaction
module.exports = {
    async up(queryInterface, Sequelize) {
      const transaction = await queryInterface.sequelize.transaction();
      try {
        await queryInterface.addColumn(
          'Person',
          'petName',
          {
            type: Sequelize.DataTypes.STRING,
          },
          { transaction },
        );
        await queryInterface.addIndex('Person', 'petName', {
          fields: 'petName',
          unique: true,
          transaction,
        });
        await transaction.commit();
      } catch (err) {
        await transaction.rollback();
        throw err;
      }
    },
    async down(queryInterface, Sequelize) {
      const transaction = await queryInterface.sequelize.transaction();
      try {
        await queryInterface.removeColumn('Person', 'petName', { transaction });
        await transaction.commit();
      } catch (err) {
        await transaction.rollback();
        throw err;
      }
    },
  };

// to create unique index
module.exports = {
    up: (queryInterface, Sequelize) => {
      queryInterface
        .createTable('Person', {
          name: Sequelize.DataTypes.STRING,
          bool: {
            type: Sequelize.DataTypes.BOOLEAN,
            defaultValue: false,
          },
        })
        .then((queryInterface, Sequelize) => {
          queryInterface.addIndex('Person', ['name', 'bool'], {
            indicesType: 'UNIQUE',
            where: { bool: 'true' },
          });
        });
    },
    down: (queryInterface, Sequelize) => {
      return queryInterface.dropTable('Person');
    },
  };

// to create foregin key relationship
// user_id: {
//     type: sequelize.INTEGER,
//     allowNull: false,
//     reference: {
//         model: 'user',
//         key: 'id'
//     }
// }

// To drop all tables
// await queryInterface.dropAllTables()

// Running migrations
// npx sequelize-cli db:migrate

// Undo migrations
// npx sequelize-cli db:migrate:undo

// SequealizedMeta table contains information about ran migrations

// create seed data
// npx sequelize-cli seed:generate --name demo-user

// run seeds data
// npx sequelize-cli db:seed:all

// undo seeds data
// npx sequelize-cli db:seed:undo