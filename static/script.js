// JavaScript to get the value of the button and update the href attribute
document.getElementById('menuBar').addEventListener('click', function(event) {
    var category = event.target.id;
    document.getElementById('news').href = '/news-category/' + category;
    document.getElementById('politics').href = '/news-category/' + category;
    document.getElementById('business').href = '/news-category/' + category;
    document.getElementById('sports').href = '/news-category/' + category;
    document.getElementById('entertainment').href = '/news-category/' + category;
});
