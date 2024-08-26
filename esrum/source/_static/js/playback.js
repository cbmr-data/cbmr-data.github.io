// Based on code by Hoàng Hà: https://codepen.io/hoanghals
(function () {
    // Convert to array since changing classes mutates a HTMLCollection
    let elements = Array.from(document.getElementsByClassName("gif"));
    for (var i = 0; i < elements.length; ++i) {
        let elem = elements[i];

        if (elem.tagName === "IMG") {
            setup = function () {
                var controlElement = document.createElement("div");
                controlElement.className = "gifcontrol loading g" + i;
                var playing = false;

                var animation = new SuperGif({
                    gif: elem,
                    progressbar_height: 0,
                    auto_play: false,
                    loop_mode: false,
                    on_end: function () {
                        playing = false;
                        controlElement.className = "gifcontrol paused";
                    }
                });

                animation.load((function (controlElement) {
                    controlElement.className = "gifcontrol paused";
                    controlElement.addEventListener("click", function () {
                        if (playing) {
                            this.pause();
                            playing = false;
                            controlElement.className = "gifcontrol paused";
                        } else {
                            this.play();
                            playing = true;
                            controlElement.className = "gifcontrol playing";
                        }
                    }.bind(this, controlElement));

                }.bind(animation))(controlElement));

                let canvas = animation.get_canvas();
                controlElement.style.width = canvas.width + "px";
                controlElement.style.height = canvas.height + "px";
                controlElement.style.left = canvas.offsetLeft + "px";

                let containerElement = canvas.parentNode;
                containerElement.appendChild(controlElement);
            }

            // check naturalHeight since complete is set on broken links
            if (elem.complete && elem.naturalHeight) {
                setup();
            } else {
                elem.onload = setup;
            }
        }
    }
})();
