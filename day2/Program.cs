//  ^       - Starts With
//  $       - Ends With
// []       - Range
// ()       - Group
//  .       - Single character once
//  +       - one or more characters in a row
//  ?       - optional preceding character match
//  \       - escape character
// \n       - New line
// \d       - Digit
// \D       - Non-digit
// \s       - White space
// \S       - non-white space
// \w       - alphanumeric/underscore character (word chars)
// \W       - non-word characters
// {x,y}    - Repeat low (x) to high (y) (no "y" means at least x, no
// {x|y}    - Alternative - x or y   
// 
// [^x]     - Anything but x (where x is whatever character you want)

using System.Text.RegularExpressions;

// See https://aka.ms/new-console-template for more information
const string str = "Game 1: 4 blue, 4 red, 16 green; 14 green, 5 red; 1 blue, 3 red, 5 green\n";
const string patternb = @"(\d* blue)";
const string patternr = @"(\d* red)";
const string patterng = @"(\d* green)";
var c = new List<MatchCollection>
{
    new Regex(patternb).Matches(str),
    new Regex(patterng).Matches(str),
    new Regex(patternr).Matches(str)
};
var d = c.SelectMany(a => a.Select(b => b)).ToList();
foreach (var v in d)
{
    Console.WriteLine(v);
}
// foreach (Match match in matches)
// {
//     foreach (var group in match.Groups)
//     {
//         Console.WriteLine(group);
//     }
// }
Console.WriteLine("Hello, World!");
