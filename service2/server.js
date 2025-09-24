const app = require("./app/app");

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Service2 is running on port ${PORT}`);
});
