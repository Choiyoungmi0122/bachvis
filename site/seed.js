// site/seed.js
const { mongoose, connectDB } = require('./mongo');
const User = require('./models/User');

async function seed() {
  await connectDB();

  const newUser = await User.create({
    prompt: '요즘 남편이랑 같이 있으면 많이 불안해져요...'
  });

  console.log('✅ 저장 완료:', newUser);

  await mongoose.disconnect();
}

seed();
