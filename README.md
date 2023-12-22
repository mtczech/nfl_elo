# nfl_elo

NFL Elo: A Historical Power Ranking of NFL Teams

You may or may not be familiar with the Elo ranking system. TLDR: It's a power ranking system commonly used in chess to determine relative player strength. My family have always been fans of the NFL, and I wanted to find out a way to combine my passion for data with a subject I am interested in and knowledgeable about. So I decided to use the Elo ranking system to calculate the strength of any NFL team at any point in time.

How The System Works

Each team starts at 1000 at the beginning of the 2002 season (2002 was chosen because it was the first year where all 32 teams were in the NFL). Whenever a team plays another team, the Elo score is recalculated for those two teams, with the winner gaining points and the loser losing points. (If there is a tie, the lower rated team gains points at the expense of the higher rated team.) If a team has a bye week, it keeps the same Elo as it had the previous week. 

To go more in depth about the math, each team has an expected score. Basically, this is what their probability is of winning a given game based on their and their opponent's Elo scores. This is calculated with the following formula:

![image](https://github.com/mtczech/nfl_elo/assets/73159403/7cab1987-8e44-419e-ac58-2228d28adc85)

where o is the opponent's Elo score and p is the player's Elo score. Once the win probabilities are calculated, we take in the actual result (1 if the team wins, 0 if the team loses, 0.5 for a tie). We then multiply the actual result by the previously calculated win probability, and then multiply by some amplifying constant (in this case 32 for the 32 teams in the league), to get the amount the Elo score goes up or down by. 

The AFC East

![image](https://github.com/mtczech/nfl_elo/assets/73159403/5143b421-a280-4b57-8709-e00ef4915e40)

The YouTube sports analyst Barry McCockiner often complains about how Tom Brady's Patriots had nobody to challenge them in their division over the course of his time with them. The data here seems to prove him correct. Although things are close in the beginning at first glance, this is misleading: Brady's Patriots won the Super Bowl the year before the data started, so they were certainly better than the teams in their division. A few seasons after, the Patriots hit a score of about 1200 and stay around that score until 350 games into our sample (sometime towards the end of the 2018-19 season). During this time, they achieve the highest score of any team in our sample: 1335.745, right before the 2008 Super Bowl. Not coincidentally, Brady's departure from the Patriots coincided with a sharp decline in the team's fortunes and the Pats have slipped back into mediocrity, having been replaced as the kings of the division by Josh Allen's Bills.

The AFC West

![image](https://github.com/mtczech/nfl_elo/assets/73159403/7d9d58e6-2dc6-4b89-b82c-ce80e86866a6)

Unlike the AFC East, the AFC West had no dominant force initially. Around 250 games in (Around 2014), a Broncos team led by Peyton Manning dominated the division for a few years. However, when they fell, Patrick Mahomes' Chiefs rose, and based on this data there is every chance they could dominate their division the same way Brady's Patriots dominated theirs.

The AFC North

![image](https://github.com/mtczech/nfl_elo/assets/73159403/04d2e0bb-d941-47d7-b67c-c8b0f514cdb1)

The AFC North has been competitive at the top, with the Ravens and Steelers consistently being average to good, and at a few points including now the Bengals being a very good team. However, there has been no doubt as to who the worst team in the division was for most of our time period. The Browns ranged from average to terrible for our entire sample, but they hit a low point when they hired head coach Hue Jackson. When he entered at the beginning of 2015, the Browns were in a hole: they had the lowest Elo score any team in the division had ever had until that point, coming in at just under 750. Jackson's first act was to grab a shovel: the 32 games of his tenure, the Browns won one. At the end, the Browns had the worst Elo score in our dataset ever: 660.65. Thankfully, they put together a few good seasons and are now simply below average.

The AFC South

![image](https://github.com/mtczech/nfl_elo/assets/73159403/15c39a4d-10b7-4d08-b087-477059ffbbb7)

Peyton Manning actually has two periods of dominance in our timeline: one with the Colts and one with the Broncos. He hit his own peak of consistent 1200s for a few years, even breaking the 1300 barrier, and his peak would be longer in our graph if not for the fact that his career started in 1998, four years before our dataset begins. Like Brady, he didn't have any major challengers during his peak. Unlike Brady, the void in his division was never filled, with all of the teams in the post-Peyton AFC South ranging from slightly above average to terrible.

The NFC East

![image](https://github.com/mtczech/nfl_elo/assets/73159403/e3c9e79a-3e08-434e-8c48-3598dca4302d)

Note: The 'Commies' are the football team that plays in Washington D.C. They were formerly known as the Redskins and the Washington Football Team before changing their name to the Commanders.

So far, the NFC East appears to be the most even division, with no team ever enjoying any period of consistent dominance apart from the Eagles for a brief period towards the beginning. Eli Manning has had a few moments leading the Giants, but he has had nowhere near the dominance of his brother over a long term. The Commies were never anything more than average, but not truly bad enough to stand out outside of the division. And if the Cowboys are America's Team, then it's a sign of how far our nation has fallen: they have been very close to average consistently.

The NFC West

![image](https://github.com/mtczech/nfl_elo/assets/73159403/57fdbc5a-8571-4295-a156-33c834d48910)

Like the NFC East, the NFC West has also been competitive for most if not all of its history. All four of the teams in the NFC West have had significant stretches as the best team in the division, but the highest high was the Seahawks' Legion of Boom around 2015 or 2016.

The NFC North

![image](https://github.com/mtczech/nfl_elo/assets/73159403/ab5c5300-4041-4a35-82da-e41c1e72df49)

For the most part, there was a lot of parity in the NFC North up until around 2010. The Bears, Packers, and Vikings were all jockeying for division supremacy, with the Lions being a long way behind. The turning point here was the 2010 NFC Championship game between the Bears and Packers, for the next five years the Packers' dominance would not be seriously challenged, but the Vikings have made things more interesting recently.

The NFC South

![image](https://github.com/mtczech/nfl_elo/assets/73159403/6aa57b9b-a2d2-4156-b256-7a9887c58957)

While the NFC South has not produced a truly dominant team, they have not produced a truly bad one either. This has led to a division where teams rise and fall in the ranks rapidly. For example, the Panthers have gone from the worst team in the division to the best by 200 points to the worst again in the space of less than a decade. Interestingly, the NFC South and AFC West are the only two divisions where every team has been on top at some point during the 20 year span and every team has been on the bottom.

Improvements to the System

There are four main improvements that could be made to this system of ranking teams. First of all, all teams start off with the same score at the beginning. This does not reflect how good the teams actually were at the beginning of the 2002 season: The defending Super Bowl champion Patriots and the "Greatest Show on Turf" Rams were much better at the time than the 1-15 Panthers or the just-created Texans. But the data has to start somewhere, and I don't want to put artificial values in. (I could, though.)

The second point to be made here is that not all games are created equal. The Super Bowl is more important than an end-of-season game between two teams who are 4-11 and have nothing to play for. If anything, the 4-11 teams have an incentive to lose: they will get a better draft pick if they do. In the same vein, if a team has gone 15-0 and already clinched home-field advantage throughout the playoffs, they will probably try to rest their best players to prevent them from getting injured. For this reason, if a 8-7 team fighting to make the playoffs beats them, it is not as big of an upset as the Elo score would suggest and might even be the expected result.

Third, for the purposes of this analysis, a win is a win. There is no difference between winning by one point and winning by fifty in our analysis. However, if we are trying to measure dominance, we might want to reward blowout wins and punish blowout losses more than close wins and close losses. 

Finally, football is an erratic game. Players can get hurt and decrease the strength of their team. Home-field advantage can give one team the edge. The Miami Dolphins can come into Green Bay in January and be at a disadvantage since they're not used to dealing with the cold, or the Packers could come into Miami early in the season and have trouble adjusting to the heat and humidity. All of these factors cannot be taken into account when you are working with a single Elo score.

However, what the Elo score is good for is spotting general trends: which teams are good and which are bad at a given time. Over the course of 20 years, we can learn a lot about the league this way.
