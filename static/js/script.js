const arrow = document.getElementsByClassName('caret-icon-fa')[0];
const comment_content = document.getElementsByClassName('visible-post-comments-content')[0];

function toggleOpenContent() {
    if (arrow.classList.contains('open')) {
        comment_content.style.display = 'none';
        arrow.classList.remove('fa-caret-up');
        arrow.classList.add('fa-caret-down');
        arrow.classList.remove('open');
    } else {
        comment_content.style.display = 'block';
        arrow.classList.remove('fa-caret-down');
        arrow.classList.add('fa-caret-up');
        arrow.classList.add('open');
    }
}

arrow.addEventListener('click', toggleOpenContent);