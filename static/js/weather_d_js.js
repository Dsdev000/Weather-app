$(document).ready(function()
  {
    $('.largenav li:nth-child(4)').addClass("active");



   /* $("input[name='temp']").change(function()
    {
      val=$(this).val();
      if(val==2)
      {
          if("{{weather.temperature}}" == $('.btn-weather > p').val())
          {
          weather_0=Math.round( ( {{ weather.temperature}}  - 32)  * (5/9));
           $('#weather').html(weather_0);

          }
        

      }
      else
      {
             if("{{weather.temperature}}" == $('.btn-weather  p').val())
          {
           $('#weather').html("{{ weather.temperature }}");
         }
      }
    });*/
           
           $('.get_temp').click(function(e)
           {
              $.ajax({
              url:'/weather_mesurement',
              data:
              {

               'chage_measuremnt':$(this).attr('id')
              },
                 success: function (response) {
                 
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                     $(".weather_panel").removeClass();
                     
                    $(".weather_main_panel").html($(response).find(".weather_panel"));
                     
              
                 
              }
            });
              e.preventDefault();
           });
   
  $("input[type='radio']").change(function (){
       
          if("{{weather_btn.d_t}}"==this.id)
          { 
           $('#search_place_address').html("{{weather_btn.city}}");
           $('#day').html("{{weather_btn.d_t}}");
           $('#description').html("{{weather_btn.description}}");
           $('#weather_img').attr('src','https://openweathermap.org/img/w/{{ weather_btn.icon }}.png');
           $('#weather').html("{{weather_btn.temperature}}<sup><sup>");
           $('#pressure').html("Pressure : {{weather_btn.pressure}} millibars");
           $('#humidity').html("Humidity : {{weather_btn.humidity}}<small>%</small>");
           $('#wind').html("Wind :  {{weather_btn.wind}} mph");
           }
         
    });
         
  });