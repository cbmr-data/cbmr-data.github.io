// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    // The maximum is exclusive and the minimum is inclusive
    return Math.floor(Math.random() * (max - min) + min);
}


function getEphemeralPort() {
    // https://en.wikipedia.org/wiki/Ephemeral_port
    return getRandomInt(49152, 65535);
}

function replaceTextContent(elem, pattern, replacement) {
    if (elem.childNodes.length) {
        elem.childNodes.forEach(function (child) {
            replaceTextContent(child, pattern, replacement);
        });
    } else if (elem.textContent) {
        elem.textContent = elem.textContent.replaceAll(pattern, replacement);
    }
};

/** Open external links in a new window */
document.querySelectorAll('a.reference.external').forEach(
    function (elem) {
        elem.target = '_blank';
    }
);
