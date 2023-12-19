function resizeIframe() {
    var container = document.getElementById('iframeContainer');
    var iframe = document.getElementById('responsiveIframe');
    var aspectRatio = 16 / 9;

    var containerWidth = container.offsetWidth;
    var newHeight = Math.floor(containerWidth / aspectRatio);

    iframe.style.width = containerWidth + 'px';
    iframe.style.height = newHeight + 'px';
}

function updateIframeSrc() {
    var iframe = document.getElementById('responsiveIframe');
    var queryString = window.location.search;
    var urlParams = new URLSearchParams(queryString);

    var id = urlParams.get('TMDB_ID');
    var season = urlParams.get('seasonNumber');
    var episode = urlParams.get('episodeNumber');

    if (season !== null && episode !== null) {
        var tvSrcUrl = `https://www.2embed.cc/embedtv/${id}&s=${season}&e=${episode}`;
        iframe.src = tvSrcUrl;
    } else {
        var movieSrcUrl = `https://www.2embed.cc/embed/${id}`;
        iframe.src = movieSrcUrl;
    }
}

window.onload = window.onresize = function () {
    resizeIframe();
    updateIframeSrc();
};