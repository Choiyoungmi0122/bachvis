// site/models/User.js
const { mongoose } = require('../mongo');

const userSchema = new mongoose.Schema({
  prompt: { type: String, required: true }
});

module.exports = mongoose.model('User', userSchema);
