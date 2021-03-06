Q1 = "select AVG(age) from Player"

Q2 = "select match_no , play_date from Match where audience >50000"
#Q2 = '''SELECT match_no, play_date FROM Match WHERE audience > 50000 ORDER BY match_no ASC;'''

#Q3 = "select team_id , COUNT(win_lose) from MatchTeamDetails where match_no>=1"
Q3 = '''SELECT team_id, COUNT(win_lose) AS Win FROM MatchTeamDetails WHERE win_lose = "W" GROUP BY team_id ORDER BY Win DESC, team_id ASC;'''

Q4 = '''SELECT match_no, play_date FROM Match WHERE stop1_sec > (SELECT AVG(stop1_sec) FROM Match) ORDER BY match_no DESC, play_date DESC;'''

Q5 = '''SELECT `Match`.`match_no`, `Team`.`name`, `Player`.`name` FROM MatchCaptain INNER JOIN Team on `MatchCaptain`.`team_id` = `Team`.`team_id` INNER JOIN Match on `MatchCaptain`.`match_no` = `Match`.`match_no` INNER JOIN Player on `MatchCaptain`.`captain` = `Player`.`player_id` ORDER BY `Match`.`match_no` ASC, `Team`.`name` ASC;'''

Q6 = '''SELECT match_no, `Player`.`name`, jersey_no From Match INNER JOIN Player on `Player`.`player_id` = `Match`.`player_of_match` ORDER BY match_no ASC;'''

Q7 = ""
