// site/mongo.js
const mongoose = require('mongoose');
require('dotenv').config();

// 👉 여기에 실제 Atlas URI 입력
const uri = process.env.MONGO_URI;

async function connectDB() {
  await mongoose.connect(uri);
  console.log('✅ MongoDB 연결 성공');
}

module.exports = { mongoose, connectDB };

