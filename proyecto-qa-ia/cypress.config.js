const { defineConfig } = require("cypress");
const fs = require('fs');
const path = require('path');

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // Crear directorio de logs si no existe
      const logsDir = path.join(__dirname, 'logs');
      if (!fs.existsSync(logsDir)) {
        fs.mkdirSync(logsDir);
      }

      // Evento para capturar resultados de tests
      on('after:run', (results) => {
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
        const logFile = path.join(logsDir, `test-results-${timestamp}.json`);
        
        const logData = {
          timestamp: new Date().toISOString(),
          totalTests: results.totalTests,
          totalPassed: results.totalPassed,
          totalFailed: results.totalFailed,
          totalPending: results.totalPending,
          totalSkipped: results.totalSkipped,
          totalDuration: results.totalDuration,
          runs: results.runs.map(run => ({
            spec: run.spec.relative,
            stats: run.stats,
            tests: run.tests.map(test => ({
              title: test.title.join(' > '),
              state: test.state,
              duration: test.duration,
              error: test.err ? {
                name: test.err.name,
                message: test.err.message,
                stack: test.err.stack
              } : null
            }))
          }))
        };

        fs.writeFileSync(logFile, JSON.stringify(logData, null, 2));
        console.log(`📊 Test results saved to: ${logFile}`);
      });

      return config;
    },
  },
});
