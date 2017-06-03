$(document).ready(function() {

    var newsBg = "url(/static/img/news-bg.png)";
    var newsBgColor = "url(/static/img/news-bg-color.png)";

    var endBg = "url(/static/img/end-bg.png)";
    var endBgColor = "url(/static/img/end-bg-color.png)";

    var alreadyBg = "url(/static/img/already.png)";
    var alreadyBgColor = "url(/static/img/already-color.png)";

    var displayLogo = "/static/img/display-logo.png";
    var displayText = "/static/img/display-text.png";
    var display = "/static/img/display.png";

    var down = "/static/img/down.png";
    var up = "/static/img/up.png";

    var like = "/static/img/like-news.png";
    var likeActive = "/static/img/like-news-active.png";

    $('#block-catalog').mousemove(function (e) {
        var target = $(e.target);
        if ($(target).hasClass('book-img')) {
            target.parent().find('.shadow-bg').slideDown();
        } else if ($(target).hasClass('img')) {
            $(this).find(".shadow-bg").slideUp();
        } else if ($(target).attr('id') === 'block-catalog') {
            $(this).find(".shadow-bg").slideUp();
        }
    });

    $('#block-search').mousemove(function (e) {
        var target = $(e.target);
        if ($(target).hasClass('book-img')) {
            target.parent().find('.shadow-bg').slideDown();
        } else if ($(target).hasClass('img')) {
            $(this).find(".shadow-bg").slideUp();
        } else if ($(target).attr('id') === 'block-search') {
            $(this).find(".shadow-bg").slideUp();
        }
    });

    $('#like-news').click(function (e) {
        var src = ($(this).attr("src") === like)
                    ? likeActive
                    : like;
        $(this).attr("src", src);

        var idNews = $(this).attr('data-id-news');

        $.ajax({
            url: "/news/news_like/",
            type: "GET",
            data: {
                id: idNews,
            },
            success: function (data) {
                $('#like-news-update').html(data);
            },
        });
    });

    $('#like-book').click(function (e) {
        var src = ($(this).attr("src") === like)
                    ? likeActive
                    : like;
        $(this).attr("src", src);

        var idBook = $(this).attr('data-id-book');

        $.ajax({
            url: "/like_book/",
            type: "GET",
            data: {
                id: idBook,
            },
            success: function (data) {
                $('#like-book-update').html(data);
            },
        });
    });

    $("#button").click(function(e) {
        if ($(this).attr("src") === down) {
            $(".shadow-header").animate({height: 820}, "fast");
            $(".main-header .block-text").slideDown("fast");
            $(".main-header .another-block-text").css("display", "none");
            $(this).attr("src", up);
        } else {
            $(".shadow-header").animate({height: 0}, "fast");
            $(".main-header .block-text").slideUp("fast");
            $(".main-header .another-block-text").css("display", "block");
            $(this).attr("src", down);
        }
    });

    $(".shadow").mouseenter(function(e) {
        var elShadow = $(e.target);
        var elPlus = $(e.target).parent().find(".plus");
        if (!elShadow.hasClass("shadow")) {
            elShadow = elShadow.parent();
            elPlus = elShadow.parent().find(".plus");
        }
        elShadow.slideUp("fast");
        elPlus.fadeIn("fast");
    });

    $(".bgc").mouseleave(function(e) {
        var elShadow = $(e.target).parent().find(".shadow");
        var elPlus = $(e.target).parent().find(".plus");
        elShadow.slideDown("fast");
        elPlus.fadeOut("fast")
    });

    $('#display').click(function(e) {
        var src = ($(this).attr("src") === displayLogo)
                    ? displayText
                    : displayLogo;
        $(this).attr("src", src);
    });
    $('#display').mouseenter(function(e) {
        $(this).attr("src", displayLogo);
    });
    $('#display').mouseleave(function(e) {
        $(this).attr("src", display);
    });

    $('.end').mouseenter(function(e) {
        $(this).css("background-image", endBgColor).animate({opacity: 1.0}, "fast");
    });
    $('.end').mouseleave(function(e) {
        $(this).css("background-image", endBg).animate({opacity:0.9}, "fast");
    });

    $('.already').mouseenter(function(e) {
        $(this).css("background-image", alreadyBgColor).animate({opacity: 1.0}, "fast");
    });
    $('.already').mouseleave(function(e) {
        $(this).css("background-image", alreadyBg).animate({opacity:0.9}, "fast");
    });

    $('#like').click(function(e) {
        var src = ($(this).attr("src") == "/static/img/like.png")
                    ? "/static/img/like-active.png" 
                    : "/static/img/like.png";
        $(this).attr("src", src);
        blink($(this));
    });

    $('#mouse').click(function(e) {
        var src = ($(this).attr("src") === "/static/img/mouse.png")
                    ? "/static/img/mouse-active.png" 
                    : "/static/img/mouse.png";
        $(this).attr("src", src);
        blink($(this));
    });

    $('#lamp').click(function(e) {
        var src = ($(this).attr("src") === "/static/img/lamp.png")
                    ? "/static/img/lamp-active.png" 
                    : "/static/img/lamp.png";
        $(this).attr("src", src);
        blink($(this));
    });

    function blink(e) {
        $(e).fadeOut();
        $(e).fadeIn();
    }

    $('.news').mouseenter(function(e) {
        $(this).css("background-image", newsBgColor).animate({opacity: 1.0}, "fast");
    });
    $('.news').mouseleave(function(e) {
        $(this).css("background-image", newsBg).animate({opacity:0.9}, "fast");
    });
    $('#email').mouseenter(function(e) {
        $(this).animate({opacity: 1.0}, "fast");
    });
    $('#email').mouseleave(function(e) {
        $(this).animate({opacity: 0.9}, "fast");
    });
    $('#locale').mouseenter(function(e) {
        $(this).animate({opacity: 1.0}, "fast");
    });
    $('#locale').mouseleave(function(e) {
        $(this).animate({opacity: 0.9}, "fast");
    });
    $('#phone').mouseenter(function(e) {
        $(this).animate({opacity: 1.0}, "fast");
    });
    $('#phone').mouseleave(function(e) {
        $(this).animate({opacity: 0.9}, "fast");
    });
    $("#ipad").mouseenter(function(e) {
        $(this).parent().animate({left: +20}, "slow");
    });
    $("#ipad").mouseleave(function(e) {
        $(this).parent().animate({left: -20}, "slow");
    });
    $("#display").mouseenter(function(e) {
        $(this).parent().animate({top: +20}, "slow");
    });
    $("#display").mouseleave(function(e) {
        $(this).parent().animate({top: -20}, "slow");
    });
    $(".nav-catalog a").click(function(e) {
        var arr = $(".nav-catalog div").toArray();
        arr.forEach(function(element) {
            var el = $(element);
            el.css("background-repeat", "no-repeat");
            el.removeClass("line");
        }, this);
        var needEl = $(e.target).parent().find("div");
        needEl.addClass("line");
        needEl.css("background-repeat", "repeat-x");

        var genre = $(this).attr('data-title');
        $.ajax({
            url: "/catalog/" + genre,
            type: "GET",
            data: {
                genre: genre,
            },
            success: function (data) {
                $('#block-catalog').html(data);
            },
        });
    });

    $('.search-type p').click(function(e) {
        var arr = $('.search-type p').toArray();
        var arrCategory = $('.search-category div').toArray();
        var type = $(this).attr('data-type');
        arrCategory.forEach(function(element) {
            var el = $(element);
            el.css('display', 'none');
        });
        if (type === 'books') {
            $('.search-books').css('display', 'block');
        } else if (type === 'users') {
            $('.search-users').css('display', 'block');
        } else if (type === 'news') {
            $('.search-news').css('display', 'block');
        }
        arr.forEach(function(element) {
            var el = $(element);
            el.removeClass('active');
        });
        $(this).addClass('active');
    });

    $('.search-users p').click(function(e) {
        var arr = $(this).parent().find('p').toArray();
        arr.forEach(function(element) {
            var el = $(element);
            el.removeClass('active');
        });
        $(this).addClass('active');
    });

    $('.search-books p').click(function(e) {
        var arr = $(this).parent().find('p').toArray();
        arr.forEach(function(element) {
            var el = $(element);
            el.removeClass('active');
        });
        $(this).addClass('active');
    });

    $('.search-news p').click(function(e) {
        var arr = $(this).parent().find('p').toArray();
        arr.forEach(function(element) {
            var el = $(element);
            el.removeClass('active');
        });
        $(this).addClass('active');
    });

    $('#search').click(function(e) {
        var text = $('#text_for_search').val().trim().toLowerCase();
        var type = $('.search-type').find('.active').attr('data-type');
        if (type === 'books') {
            var category = $('.search-books').find('.active').attr('data-cat');
        } else if (type === 'users') {
            var category = $('.search-users').find('.active').attr('data-cat');
        } else if (type === 'news') {
            var category = $('.search-news').find('.active').attr('data-cat');
        }
        if (text !== "" || category === "list_books_taken" || category === "list_books_favorites" || category === "debt" || category === "debt-users") {
            $.ajax({
            url: "/search/" + type,
            type: "GET",
            data: {
                type: type,
                category: category,
                text: text,
            },
            success: function (data) {
                $('#block-search').html(data);
            },
        });
        } else {
            $('#block-search').html("Введите данные");
        }
    });

    function addRemoveBook(e) {
        var v = $(e.target);
        if ($(v).hasClass('link-book')) {
            var bookId = $(v).attr('data-id');
            var targetLink = $(v).closest('.shadow-bg').find('#mark-link');
         $.ajax({
            url: "/link_book/",
            type: "GET",
            data: {
                id: bookId,
            },
            success: function (data) {
                $(targetLink).html('<h3>' + data + '</h3>');
            },
        });
        } else if ($(v).hasClass('like-book')) {
            var bookId = $(v).attr('data-id');
            var targetLike = $(v).closest('.shadow-bg').find('#mark-like');
            $.ajax({
                url: "/like_book/",
                type: "GET",
                data: {
                    id: bookId,
                },
                success: function (data) {
                    $(targetLike).html('<h3>' + data + '</h3>');
                },
            });
        }
    }

    $('#block-catalog').click(function(e) {
        addRemoveBook(e);
    });

    $('#block-search').click(function(e) {
        addRemoveBook(e);
    });

    $('#text_for_search').keyup(function (e) {
        var val = $(this).val().trim().toLowerCase();
        var size = val.length;
        if (size > 2) {
            var type = $('.search-type').find('.active').attr('data-type');
            $.ajax({
                url: "/live_search/",
                type: "GET",
                data: {
                    text: val,
                    type: type,
                },
                success: function (data) {
                    $('#live-search').html(data);
                },
            });
        } else {
            $("#live-search").empty();
        }
    });

    $('#live-search').click(function(e) {
        var target = $(e.target);
        var id = target.attr('data-id');
        var type = target.attr('data-type');
        $.ajax({
            url: "/search/" + type,
            type: "GET",
            data: {
                type: type,
                id: id,
            },
            success: function (data) {
                $('#block-search').html(data);
            },
        });
    });
});