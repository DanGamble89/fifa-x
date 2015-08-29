const srcFolder = './assets';
const distFolder = './fifa/static';
const templateFolder = './fifa/jinja';

export default {
  bower: {
    path: './bower_components'
  },
  css: {
    dist: `${distFolder}/css`
  },
  images: {
    dist: `${distFolder}/images`,
    src: [
      `${srcFolder}/images/**/*`
    ]
  },
  js: {
    dist: `${distFolder}/js`,
    src: [
      `${srcFolder}/*.js`,
      `${srcFolder}/**/*.js`
    ]
  },
  html: {
    path: templateFolder,
    src: [
      `${templateFolder}/*.html`,
      `${templateFolder}/**/*.html`
    ]
  },
  sass: {
    src: [
      `${srcFolder}/scss/*.scss`,
      `${srcFolder}/scss/**/*.scss`
    ]
  },
  watchify: {
    fileIn: `${srcFolder}/js/main.js`,
    fileOut: `main.js`,
    folderIn: `${srcFolder}/js`,
    folderOut: `${distFolder}/js`
  }
};
