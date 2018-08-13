        function get_movies() {
            $.ajax({
                type: "POST",
                url: "/get_movies",
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    $("#movie_table").find("tr:gt(0)").remove();
                    var json = jQuery.parseJSON(response)
                    var movie_data = '';
                     $.each(json.movies, function(key, value) {
                        movie_data += '<tr>';
                        movie_data += '<td>'+value.name_eng+'</td>';
                        movie_data += '<td>'+value.name_rus+'</td>';
                        movie_data += '<td>'+value.year+'</td>';
                        movie_data += '<td>'+value.genres+'</td>';
                        movie_data += '<td>'+value.countries+'</td>';
                        movie_data += '<td>'+value.directors+'</td>';
                        movie_data += '<td>'+value.writers+'</td>';
                        movie_data += '<td>'+value.rus_prem+'</td>';
                        movie_data += '<td><a href='+value.url+'data-popup-info="enabled">Go to Kinopoisk.ru</a></td>';
                        movie_data += '</tr>';

                    
                    $('#movie_table tbody').html(movie_data)})
                    
                }
            });
        }