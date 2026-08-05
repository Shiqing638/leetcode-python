class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        m = len(votes[0]) # how many teams and rank

        rank = {team: [0] * m for team in votes[0]}

        for vote in votes:
            for i, team in enumerate(vote):
                rank[team][i] += 1
        teams = list(votes[0]) # str immutable

        def getKey(team):
            count = []
            for num in rank[team]:
                count.append(-num)
            return (count, team)

        teams.sort(key = getKey)
        return "".join(teams)