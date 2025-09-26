const fs = require("fs");

class SharedStorageService {
  constructor() {
    this.filePath = process.env.SHARED_STORAGE_PATH || "./vstorage";
  }

  async appendStatus(statusMessage) {
    await fs.promises.appendFile(this.filePath, `${statusMessage}\n`, "utf8");
  }
}

module.exports = SharedStorageService;
