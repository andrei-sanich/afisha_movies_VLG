        function get_movies() {
            $.ajax({
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
                        movie_data += '<td>'+value.genres.slice(1, -1)+'</td>';
                        movie_data += '<td>'+value.countries.slice(1, -1)+'</td>';
                        movie_data += '<td>'+value.directors.replace(/[{}""]/g, "")+'</td>';
                        movie_data += '<td>'+value.writers.replace(/[{}""]/g, "")+'</td>';
                        movie_data += '<td>'+value.rus_prem+'</td>';
                        movie_data += '<td><a href='+value.url+'data-popup-info="enabled">Go to Kinopoisk.ru</a></td>';
                        movie_data += '</tr>';

                    
                    $('#movie_table tbody').html(movie_data)})
                    
                }
            });
        }