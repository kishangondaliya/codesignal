/*Please add ; after each select statement*/
CREATE PROCEDURE stringsStatistics()
BEGIN
	DROP TABLE IF EXISTS temp;
     CREATE temporary TABLE temp(
          str varchar(255) default null,
          letter varchar(55) default null,
          cnt int default null
          );

     INSERT INTO temp
        select str, 'a', LENGTH(str) - LENGTH(REPLACE(str, 'a', '')) as `number` from strs
          UNION
        select str, 'b', LENGTH(str) - LENGTH(REPLACE(str, 'b', '')) as `number` from strs
          UNION
               select str, 'c', LENGTH(str) - LENGTH(REPLACE(str, 'c', '')) as `number` from strs
          UNION
        select str, 'd', LENGTH(str) - LENGTH(REPLACE(str, 'd', '')) as `number` from strs
          UNION 
        select str, 'e', LENGTH(str) - LENGTH(REPLACE(str, 'e', '')) as `number` from strs
          UNION
        select str, 'f', LENGTH(str) - LENGTH(REPLACE(str, 'f', '')) as `number` from strs
          UNION
        select str, 'g', LENGTH(str) - LENGTH(REPLACE(str, 'g', '')) as `number` from strs
          UNION
        select str, 'h', LENGTH(str) - LENGTH(REPLACE(str, 'h', '')) as `number` from strs
          UNION
        select str, 'i', LENGTH(str) - LENGTH(REPLACE(str, 'i', '')) as `number` from strs
          UNION
        select str, 'j', LENGTH(str) - LENGTH(REPLACE(str, 'j', '')) as `number` from strs
          UNION
        select str, 'k', LENGTH(str) - LENGTH(REPLACE(str, 'k', '')) as `number` from strs
          UNION
        select str, 'l', LENGTH(str) - LENGTH(REPLACE(str, 'l', '')) as `number` from strs
          UNION
        select str, 'm', LENGTH(str) - LENGTH(REPLACE(str, 'm', '')) as `number` from strs
          UNION
        select str, 'n', LENGTH(str) - LENGTH(REPLACE(str, 'n', '')) as `number` from strs          UNION
        select str, 'o', LENGTH(str) - LENGTH(REPLACE(str, 'o', '')) as `number` from strs
          UNION
        select str, 'p', LENGTH(str) - LENGTH(REPLACE(str, 'p', '')) as `number` from strs          UNION
        select str, 'q', LENGTH(str) - LENGTH(REPLACE(str, 'q', '')) as `number` from strs
          UNION
        select str, 'r', LENGTH(str) - LENGTH(REPLACE(str, 'r', '')) as `number` from strs
          UNION
        select str, 's', LENGTH(str) - LENGTH(REPLACE(str, 's', '')) as `number` from strs
        UNION
        select str, 't', LENGTH(str) - LENGTH(REPLACE(str, 't', '')) as `number` from strs
      UNION
        select str, 'u', LENGTH(str) - LENGTH(REPLACE(str, 'u', '')) as `number` from strs
  UNION
        select str, 'v', LENGTH(str) - LENGTH(REPLACE(str, 'v', '')) as `number` from strs
  UNION
        select str, 'w', LENGTH(str) - LENGTH(REPLACE(str, 'w', '')) as `number` from strs
  UNION
        select str, 'x', LENGTH(str) - LENGTH(REPLACE(str, 'x', '')) as `number` from strs
  UNION
        select str, 'y', LENGTH(str) - LENGTH(REPLACE(str, 'y', '')) as `number` from strs
  UNION
        select str, 'z', LENGTH(str) - LENGTH(REPLACE(str, 'z', '')) as `number` from strs

;



     DROP TABLE IF EXISTS total;
     CREATE TABLE total (letter varchar(255) default null, total int default null);    
     INSERT INTO total
     SELECT letter, sum(cnt) as total
     FROM temp
     group by letter
     having sum(cnt) >= 1;

     DROP TABLE IF EXISTS occurrence;
     CREATE TABLE occurrence (letter varchar(255) default null, number int default null);    

     INSERT INTO occurrence
     SELECT DISTINCT letter, count(letter)
     FROM temp
     where cnt > 0
     GROUP by letter;
     
     
     DROP TABLE IF EXISTS max_occurrence;
     CREATE TABLE max_occurrence (letter varchar(255) default null, number int default null);

     INSERT INTO max_occurrence
     SELECT letter, max(cnt) as max_occurence
     FROM temp 
     where cnt > 0
     GROUP by letter;

     DROP TABLE IF EXISTS max_occurrence_reached;
     CREATE TABLE max_occurrence_reached (letter varchar(255) default null, number int default null);
     
     INSERT INTO max_occurrence_reached
     SELECT tt.letter, COUNT(*) as mor
     FROM (
          SELECT t.letter, t.cnt
          FROM temp t
          JOIN max_occurrence mo
          ON mo.letter = t.letter AND mo.number = t.cnt
     ) tt
     group by tt.letter;
     

     SELECT tt.letter, tt.total, o.number as occurrence, mo.number as max_occurrence, mor.number as max_occurrence_reached
     FROM total tt
     join occurrence o
     ON o.letter=tt.letter
     JOIN max_occurrence mo
     on tt.letter=mo.letter
     JOIN max_occurrence_reached mor
     ON tt.letter=mor.letter
     ORDER BY tt.letter;


END
     
     -- https://stackoverflow.com/questions/29967280/count-number-of-unique-characters-in-a-string
     
