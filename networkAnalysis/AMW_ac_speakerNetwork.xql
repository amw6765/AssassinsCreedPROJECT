xquery version "3.1";
declare variable $ThisFileContent :=
string-join(
let $ac := doc('/db/assassinsCreed/assassinscreedodyssey.xml')
let $chapter := $ac//chapterNum
let $acSpeakers := $chapter//speaker ! normalize-space() ! substring-before(., ":") => distinct-values()
for $a in $acSpeakers
let $acTitles := $chapter[.//speaker ! normalize-space() ! substring-before(., ":") = $a]//chapTitles ! normalize-space() => distinct-values()
for $t in $acTitles
let $otherSpeakers := $chapter[.//speaker ! normalize-space() ! substring-before(., ":") = $a][.//chapTitles ! normalize-space() = $t]//speaker
for $o in $otherSpeakers
where $o ! substring-before(., ":") != $a
return
    concat($a, "&#x9;", $t, "&#x9;", $o ! substring-before(., ":")), "&#10;");
    (: $ThisFileContent :)
   
    
    
let $filename := "AMW_ac_speakerNetwork.tsv"
let $doc-db-uri := xmldb:store("/db/assassinsCreed-queries/", $filename, $ThisFileContent, "text/plain")
return $doc-db-uri
(: View this SVG at http://newtfire.org:8338/exist/rest/db/amw6765/AMW_ac_TSV20.tsv  :)

