'use strict'
Object.defineProperty(exports, '__esModule', { value: true })
var fs = require('fs')
var path = require('path')
var faker_1 = require('@faker-js/faker')
var data_1 = require('./data')
var tasks = Array.from({ length: 100 }, function () {
    return {
        id: 'Document-'.concat(
            faker_1.faker.number.int({ min: 1000, max: 9999 })
        ),
        dimension: ''.concat(
            faker_1.faker.number.int({ min: 1, max: 100 }),
            ' MB'
        ),
        types: faker_1.faker.helpers.arrayElement(data_1.types).value,
        status: faker_1.faker.helpers.arrayElement(data_1.statuses).value,
        uploadTime: faker_1.faker.date.past().toISOString(),
    }
})
fs.writeFileSync(
    path.join(__dirname, 'tasks.json'),
    JSON.stringify(tasks, null, 2)
)
console.log('✅ Tasks data generated.')
