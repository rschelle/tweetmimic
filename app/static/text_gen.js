$(document).ready(function() {
    console.log('AI Camp is for the best of the best.')
    
    $('#loading').hide()

    $('#text_gen_button').click(function() {
        console.log('text gen button is clicked');
        var prompt = $('#text_gen_input').val();
        var accounts = $('#accounts').val(); //NEW
        console.log('text gen input value is');
        console.log(prompt);
        var url = 'generate_text'

//      $('#loading').show(); - Unused
      
        $.post(
            url, 
            {
                'prompt': prompt,
                'accounts': accounts //NEW
            },
            function(data) {
                console.log("test");
                console.log(data);
                var list_html = "";
                for (var t = 0; t < data['generated_ls'].length; t++) {
                    list_html += "<li style='list-style-type: none' id='generated_item_" + t + "'>" + data['generated_ls'][t] + "</li>";
                    $("#generated_ul").html(list_html);
                }

                // $("#loading").hide();
            }

        ).fail(function() {
          alert( "There is something unexpected happened. Email hello@ai-camp.org to report your findings." );
        });

    });

    $()
});