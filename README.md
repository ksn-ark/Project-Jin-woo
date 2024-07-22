# Project S Levelling

name is a tad cringe but the goal is noble enough to negate it imo.
naturally, sl & opm inspired.

# Implementations

- mobile app, watch app and finally web app, all three should sync and integrate as seamlessly as possible

- watch app functionalities should have redundant substitutes on both mobile and web app, either through manual routines or otherwise

# Features

## Media Controls Wrapper

- media controls wrapper for the watch app (which WILL have a loop toggle adjust button, same on the notification bar for the mobile app), mainly support for spotify with some general support for mp3 players.

## Jog Route Mapping

- jog route mapping, gonna use google maps for this one, like distance caluclations, elevation calculations, time, saved routes, edit routes, share routes, whole shebang

## Articles Section

- general health tips, a little articles section from reliable sources, should be good

## Custom C-GPT

- have a little ai mentor that provides encouragement, but generally avoids any specific instructions or information so as to avoid misinformation/ai hallucinations.
- gonna make/use a custom gpt for this one

## Game System

### Glossary

#### Levels

- Level - indicates total experience/time invested. Cannot decrease
- Exp Points - Gained through doing, causes Level to increment at fixed thresholds.

#### Stats

- Base Stats - Strength, Endurance & Flexibility. Abstract representation of physical fitness. Can decrease.
- Fixed-stat points - Only allocatable to the respective Base Stat, i.e Strength etc.
- Free-stat points - Freely allocatable to a Base Stat of the player's choice.

#### Rank

- An abstract representation of physical wellness & fitness. Incremented through consistency and effort.

#### Goals

- Daily Goal - A fixed total goal of an exercise to be cleared within the day.
- Weekly Goal - A fixed total goal of activities to be cleared within the week.

#### Rewards

- Daily Reward - Fixed reward earnt by clearing a set amount of Daily Goal's within the day.
- Weekly Reward - Fixed reward earnt by clearing a set amount of Weekly Goal's within the week.

#### Levelling system

- Initial Level = 0
- Exp required to be level x = 0.9\*x²
- User given standard progression would hit level 256 after a week in S-Rank

#### Stat system

- 1 Stat point is lost from each base stat every week from the second consecutive week of inactivity.

## Daily Goals

<table >
  <thead>
    <tr>
      <th rowspan="2" >Default Excercises</th>
      <th rowspan="2" >Target Area</th>
      <th colspan="6" style="text-align: center;">Variations by rank</th>
      <th rowspan="2" >Relevant stat</th>
    </tr>
    <tr >
    <th>E</th>
    <th>D</th>
    <th>C</th>
    <th>B</th>
    <th>A</th>
    <th>S</th>
    </tr>
  </thead>
  <thead></thead>
  <tbody>
    <tr >
      <td>Push-Ups (x10)</td>
      <td rowspan="2">Upper-Body</td>
      <td>Wall</td>
      <td>Wall</td>
      <td>Incline</td>
      <td>Incline</td>
      <td>Knee</td>
      <td>Full</td>
      <td>Strength</td>
    </tr>
    <tr>
      <td>Pull-Ups (x10)</td>
      <td>Navel</td>
      <td>Navel</td>
      <td>Torso</td>
      <td>Sternum</td>
      <td>Assisted</td>
      <td>Full</td>
      <td>Strength</td>
    </tr>
    <tr >
      <td>Squats (x10)</td>
      <td>Lower-Body</td>
      <td>Assisted</td>
      <td>Assisted</td>
      <td>Assisted Deep</td>
      <td>Standard</td>
      <td>Standard</td>
      <td>Deep</td>
      <td>Strength</td>
    </tr>
    <tr >
      <td>Hang/Plank</td>
      <td>Upper-Body</td>
      <td>10s</td>
      <td>20s</td>
      <td>30s</td>
      <td>40s</td>
      <td>50s</td>
      <td>60s</td>
      <td>Stamina</td>
    </tr>
    <tr >
      <td>Jog</td>
      <td>Lower-Body</td>
      <td>100m</td>
      <td>100m</td>
      <td>200m</td>
      <td>300m</td>
      <td>400m</td>
      <td>500m</td>
      <td>Stamina</td>
    </tr>
    <tr>
      <td>
        Sitting / Standing <br />
        Cresent Moon Stretch
      </td>
      <td>Upper-Body</td>
      <td>10 reps</td>
      <td>10 reps</td>
      <td>20 reps</td>
      <td>40 reps</td>
      <td>60 reps</td>
      <td>60 reps</td>
      <td>Flexibility</td>
    </tr>
    <tr >
      <td>
        Standing <br />
        Quadricep Stretch
      </td>
      <td>Lower-Body</td>
      <td>10 reps</td>
      <td>10 reps</td>
      <td>20 reps</td>
      <td>40 reps</td>
      <td>60 reps</td>
      <td>60 reps</td>
      <td>Flexibility</td>
    </tr>
  </tbody>
</table>

## Weekly Goals

<table>
  <thead>
    <tr>
      <th rowspan="2">Default Excercises</th>
      <th colspan="6" style="text-align: center;">Variations by rank</th>
    </tr>
    <tr>
      <th>E</th>
      <th>D</th>
      <th>C</th>
      <th>B</th>
      <th>A</th>
      <th>S</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Daily goals</td>
      <td>1 day</td>
      <td>2 days</td>
      <td>3 days</td>
      <td>4 days</td>
      <td>5 days</td>
      <td>6 days</td>
    </tr>
    <tr>
      <td>Steps</td>
      <td>500 steps</td>
      <td>1000 steps</td>
      <td>1500 steps</td>
      <td>2000 steps</td>
      <td>2500 steps</td>
      <td>3000 steps</td>
    </tr>
    <tr>
      <td>Sleep hours</td>
      <td>28 hours</td>
      <td>32 hours</td>
      <td>36 hours</td>
      <td>40 hours</td>
      <td>45 hours</td>
      <td>49 hours</td>
    </tr>
  </tbody>
</table>

## Rewards

<table>
  <thead>
    <tr>
      <th rowspan="2" colspan="2">Reward types</th>
      <th colspan="6" style="text-align: center;">Variations by rank</th>
    </tr>
    <tr>
      <th>E</th>
      <th>D</th>
      <th>C</th>
      <th>B</th>
      <th>A</th>
      <th>S</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Daily rewards</td>
      <td>fixed-stat points</td>
      <td>+1</td>
      <td>+2</td>
      <td>+3</td>
      <td>+4</td>
      <td>+5</td>
      <td>+6</td>
    </tr>
    <tr>
      <td>exp points</td>
      <td>+100</td>
      <td>+200</td>
      <td>+300</td>
      <td>+400</td>
      <td>+500</td>
      <td>+600</td>
    </tr>
    <tr>
      <td>bonus points</td>
      <td colspan="6" style="text-align: center;">1 daily goal completed for each stat = +2 free-stat points</td>
    </tr>
    <tr>
      <td rowspan="3">Weekly rewards</td>
      <td>free-stat points</td>
      <td>+3</td>
      <td>+6</td>
      <td>+9</td>
      <td>+12</td>
      <td>+15</td>
      <td>+18</td>
    </tr>
    <tr>
      <td>exp points</td>
      <td>+1000</td>
      <td>+2000</td>
      <td>+3000</td>
      <td>+4000</td>
      <td>+5000</td>
      <td>+6000</td>
    </tr>
    <tr>
      <td>bonus stat points</td>
      <td colspan="6" style="text-align: center;">1 x weekly streak + 1 x daily count</td>
    </tr>
    <tr>
      <td colspan="1">bonus multiplier</td>
      <td colspan="7" style="text-align: center;">2x to a reward set if triple relevant requirements completed</td>
    </tr>
  </tbody>
</table>

## Ranking

<table>
  <thead>
    <tr>
      <th>Rank</th>
      <th>Promotion Requirements</th>
      <th>Demotion Requirements</th>
      <th>Dailies Required Per Week</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>E</th>
      <td>null</td>
      <td>12 month missed streak</td>
      <td>1</td>
    </tr>
    <tr>
      <th>D</th>
      <td>2 weeks active streak</td>
      <td>6 month missed streak</td>
      <td>2</td>
    </tr>
    <tr>
      <th>C</th>
      <td>2 weeks active streak</td>
      <td>4 month missed streak</td>
      <td>3</td>
    </tr>
    <tr>
      <th>B</th>
      <td>3 weeks active streak</td>
      <td>2 month missed streak</td>
      <td>4</td>
    </tr>
    <tr>
      <th>A</th>
      <td>4 weeks active streak</td>
      <td>1 month missed streak</td>
      <td>5</td>
    </tr>
    <tr>
      <th>S</th>
      <td>5 weeks active streak</td>
      <td>null</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
