interface LeagueTableRow  {
    TeamName: string;
    LastFiveGames: string;
}

// TODO: 
abstract class Row {
    /** For string index access | could rewrite props, handle carefully*/
    [key: string]: any; 
    protected Rank: string|number;
    protected TeamName: string
    constructor(){
        this.Rank = -1
        this.TeamName = ""
    }
}

class LastFiveRow extends Row {
    LastFive: string
    constructor(){
        super()
        this.LastFive = ""
    }
}
class TopPlayerRow {
    /** For string index access | could rewrite props, handle carefully*/
    [key: string]: any; 
    PlayerName: string
    TeamName: string
    Goals: string
    Penalties: string
    FirstGoals: string
    constructor(){
        this.PlayerName = ""
        this.TeamName = ""
        this.Goals = ""
        this.Penalties = ""
        this.FirstGoals = ""
    }
}

class OverUnderRow extends Row {
    MatchesPlayed: string
    Goals_0: string
    Goals_1: string
    Goals_2: string
    Goals_3: string
    Goals_4: string
    Goals_5: string
    Goals_6: string
    Goals_7: string
    GoalsOver_7: string
    Avg: string
    constructor(){
        super()
        this.MatchesPlayed = ""
        this.Goals_0 = ""
        this.Goals_1 = ""
        this.Goals_2 = ""
        this.Goals_3 = ""
        this.Goals_4 = ""
        this.Goals_5 = ""
        this.Goals_6 = ""
        this.Goals_7 = ""
        this.GoalsOver_7 = ""
        this.Avg = ""
    }
}
class WideRow extends Row {
    MatchesPlayed_T: string
    Wins_T: string
    Draws_T: string
    Losses_T: string
    GoalsFor_T: string
    GoalsAgainst_T: string
    
    MatchesPlayed_H: string
    Wins_H: string
    Draws_H: string
    Losses_H: string
    GoalsFor_H: string
    GoalsAgainst_H: string

    MatchesPlayed_A: string
    Wins_A: string
    Draws_A: string
    Losses_A: string
    GoalsFor_A: string
    GoalsAgainst_A: string

    GoalDifference: string
    Points: string

    constructor(){
        super()
        this.MatchesPlayed_T = ""
        this.Wins_T = ""
        this.Draws_T = ""
        this.Losses_T = ""
        this.GoalsFor_T = ""
        this.GoalsAgainst_T = ""
        this.MatchesPlayed_H = ""
        this.Wins_H = ""
        this.Draws_H = ""
        this.Losses_H = ""
        this.GoalsFor_H = ""
        this.GoalsAgainst_H = ""
        this.MatchesPlayed_A = ""
        this.Wins_A = ""
        this.Draws_A = ""
        this.Losses_A = ""
        this.GoalsFor_A = ""
        this.GoalsAgainst_A = ""
        this.GoalDifference = ""
        this.Points = ""
    }
}


export { LeagueTableRow, LastFiveRow, TopPlayerRow, OverUnderRow, WideRow }