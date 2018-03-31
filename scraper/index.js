const request = require('request');
const cheerio = require('cheerio');

var idioms = {};


request('http://www.myenglishpages.com/site_php_files/vocabulary-lesson-idioms-alphabetical-order.php?letter=a', function(error, response, html) {
   if (!error && response.statusCode == 200) {
      var idiom = ""; 
      var idiomFinal = [];
      var $ = cheerio.load(html);
      $('em').remove();
      $('a').remove();
      $('br').replaceWith('\n');
      $('hr').replaceWith('\n');
      $('blockquote').find('div').each(function(i, element) {
         // var brSp = /<br\s*\/?>/i;
         
		   $(this).find('br').replaceWith('\n');
		   $(this).find('hr').replaceWith('\n');

         idiom = $(this).prev().text().trim().split('\n');
         idioms[idiom[0]] = idiom[1];
      });


      var j = 0;
      for (i in idiom) {
         if (idiom[i].substring(0, 8) !== "Category"
               && idiom[i].substring(0, 8) !== "See more"
               && idiom[i].substring(0, 4) !== "(See"
               && idiom[i].trim().length !== 0) {
            idiomFinal[j] = idiom[i];
            j++;
         }
      }

      for (i = 0; i < idiomFinal.length; i += 2) {
         idioms[idiomFinal[i]] = idiomFinal[i + 1];
      }

      var json = JSON.stringify(idioms, null, 2);
      console.log(json);
   }
});

