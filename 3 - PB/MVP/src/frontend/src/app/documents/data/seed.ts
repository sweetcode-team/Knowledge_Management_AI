import fs from "fs"
import path from "path"
import { faker } from "@faker-js/faker"

import { types, statuses } from "./data"

const tasks = Array.from({ length: 100 }, () => ({
  id: `Document-${faker.number.int({ min: 1000, max: 9999 })}`,
  dimension: `${faker.number.int({ min: 1, max: 100 })} MB`,
  types: faker.helpers.arrayElement(types).value,
  status: faker.helpers.arrayElement(statuses).value,
  uploadTime: faker.date.past().toISOString(),
}))

fs.writeFileSync(
  path.join(__dirname, "tasks.json"),
  JSON.stringify(tasks, null, 2)
)

console.log("✅ Tasks data generated.")
