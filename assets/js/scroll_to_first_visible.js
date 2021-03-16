function scroll_to_first_visible(selector) {
    var visible_selector = selector + ':visible:first';
    $(visible_selector)[0].scrollIntoView();
}