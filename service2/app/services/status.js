const os = require('os');

class StatusService {
  constructor() {
  }

  _getTimestamp() {
    return new Date().toISOString().split('.')[0] + 'Z';
  }

  _getUptimeHours() {
    const uptimeSeconds = os.uptime();
    return (uptimeSeconds / 3600).toFixed(3);
  }

  _getFreeDiskMB() {
    const { execSync } = require('child_process');
    const dfOutput = execSync('df / | tail -1', { encoding: 'utf8' });
    const columns = dfOutput.trim().split(/\s+/);
    const availableKB = parseInt(columns[3]);
    return (availableKB / 1024).toFixed(2);
  }

  getSystemStatus() {
    const timestamp = this._getTimestamp();
    const uptimeHours = this._getUptimeHours();
    const freeDiskMB = this._getFreeDiskMB();
    
    return `${timestamp}: uptime ${uptimeHours} hours, free disk in root: ${freeDiskMB} MBytes`;
  }
}

module.exports = StatusService;