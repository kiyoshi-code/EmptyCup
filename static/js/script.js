const img1 = document.getElementById('imgButton');
let toggled1 = false;
img1.addEventListener('click', () => {
  toggled1 = !toggled1;
  img1.src = toggled1 ? 'icons/shorlist.png' : 'icons/not shortlisted.png';

});

const img2 = document.getElementById('shortlistButton');
let toggled2 = false;
img2.addEventListener('click', () => {
  toggled2 = !toggled2;
  img2.src = toggled2 ? 'icons/shorlisted-logo.png' : 'icons/shortlist logo.png';

  const sections = document.querySelectorAll('sections');
  sections.forEach(section => {
    const imgs = section.querySelector('img');
    const img = imgs[2];
    const containsImage = img && img.src.includes('icons/shortlist.png');

    if (toggled2 && containsImage) {
      section.style.display = 'block';
    } else {
      section.style.display = 'none';
    }
  });
});
