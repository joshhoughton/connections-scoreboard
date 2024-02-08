// $(document).ready(function() {

//     console.log("table-functions.js loaded");
//     var highestScore = 0;
//     var highestScoreUser = null;

//     // Assuming each row represents a puzzle and each user score is in a table cell with class 'user-score'
//     $('.scores-table tr').each(function() {
//         var userScore = parseInt($(this).find('.user-score').text(), 10);
//         var userName = $(this).find('.user-name').text();
//         console.log(userName, userScore, highestScore, highestScoreUser);
//         if (userScore > highestScore) {
//             highestScore = userScore;
//             highestScoreUser = userName;
//         }
//     });

//     console.log("Highest score:", highestScore);
//     console.log("User with highest score:", highestScoreUser);

//     // Assuming you have a CSS class 'highlight' that styles the row
//     if (highestScoreUser) {
//         $('.puzzles-table tr').each(function() {
//             var userName = $(this).find('.user-name').text();
//             if (userName === highestScoreUser) {
//                 $(this).addClass('highlight');
//             }
//         });
//     }
// });
