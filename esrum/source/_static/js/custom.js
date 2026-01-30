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

function getOpenPort() {
    // Ports currently open on compute nodes
    return getRandomInt(8800, 9000);
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

/**
 * Return list of lambda functions that replace `pattern` in element
 * text, while supporting repeated invocations.
 */
function createElementUpdaters(elem, pattern) {
    const elems = [];
    if (elem.childNodes.length) {
        elem.childNodes.forEach(function (child) {
            elems.push(createElementUpdaters(child, pattern));
        });
    } else if (elem.textContent && elem.textContent.includes(pattern)) {
        const updater = (elem, content) => {
            return (replacement) => {
                elem.textContent = content.replaceAll(pattern, replacement);
            }
        };

        elems.push(updater(elem, elem.textContent));
    }

    if (elem.nodeName == 'A' && elem.href && elem.href.includes(pattern)) {
        const updater = (elem, content) => {
            return (replacement) => {
                elem.href = content.replaceAll(pattern, replacement);
            }
        };

        elems.push(updater(elem, elem.href));
    }

    return elems.flat();

};

/** Open external links in a new window */
let origin = (new URL(document.URL)).origin;
document.querySelectorAll('a.reference.external').forEach(
    function (elem) {
        if (new URL(elem.href).origin !== origin) {
            elem.target = '_blank';
        }
    }
);
