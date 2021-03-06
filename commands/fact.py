import random

from discord.ext import commands
from discord.ext.commands import Context, Bot

from utils.aliases import get_name_string

LONG_HELP_TEXT = """
Selects a random "interesting" "fact".
"""

SHORT_HELP_TEXT = """Information!"""


class Fact(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.options = [
            "The billionth digit of Pi is 9.",
            "Humans can survive underwater. But not for very long.",
            "A nanosecond lasts one billionth of a second.",
            "Honey does not spoil.",
            "The atomic weight of Germanium is 72.64.",
            "An ostrich's eye is bigger than its brain.",
            "Rats cannot throw up.",
            "Iguanas can stay underwater for 28.7 minutes.",
            "The moon orbits the Earth every 27.32 days.",
            "A gallon of water weighs 8.34 pounds.",
            "According to Norse legend, thunder god Thor's chariot was pulled across the sky by two goats.",
            "Tungsten has the highest melting point of any metal, at 3,410 degrees Celsius.",
            "Gently cleaning the tongue twice a day is the most effective way to fight bad breath.",
            "The Tariff Act of 1789, established to protect domestic manufacture, was the second statute ever enacted by the United States government.",
            "The value of Pi is the ratio of any circle's circumference to its diameter in Euclidean space.",
            "The Mexican-American War ended in 1848 with the signing of the Treaty of Guadalupe Hidalgo.",
            "In 1879, Sandford Fleming first proposed the adoption of worldwide standardized time zones at the Royal Canadian Institute.",
            "Marie Curie invented the theory of radioactivity, the treatment of radioactivity, and dying of radioactivity.",
            "Hot water freezes quicker than cold water.",
            "Polymerase I polypeptide A is a human gene. The shortened gene name is POLR1A",
            "The Sun's mass is 330,330 times larger than Earth's and has a volume 1.3 million times larger.",
            "Dental floss has superb tensile strength.",
            "One comes before two comes before 60 comes after 12 comes before six trillion comes after 504.",
            "The first person to prove that cow's milk is drinkable was very, very thirsty.",
            "Vulcanologists are experts in the study of volcanoes.",
            "In Victorian England, a commoner was not allowed to look directly at the Queen, due to a belief at the time that the poor had the ability to steal thoughts. Science now believes that less than 4% of poor people are able to do this.",
            "In Greek myth, Prometheus stole fire from the Gods and gave it to humankind.",
            "The Schrödinger's cat paradox outlines a situation in which a cat in a box must be considered, for all intents and purposes, simultaneously alive and dead.",
            "The plural of 'surgeon general' is 'surgeons general'.",
            "Contrary to popular belief, the Eskimo does not have one hundred different words for snow.",
            "Diamonds are made when coal is put under intense pressure.",
            "Halley's Comet can be viewed orbiting Earth every 76 years.",
            "The first commercial airline flight took to the air in 1914.",
            "Edmund Hillary was the first person to climb Mount Everest.",
            "Apollo is the best bot.",
            "Apollo is far superior to the irc bot.",
            "The whip was the first man-made invention to break the sound barrier.",
            "Giraffes are around 6 feet tall when born.",
            "The longest-observed rainbow was seen over Sheffield for six hours in March 1994.",
            "At a hunting party in 1807 Napoleon was chased by a horde of tame rabbits who mistakenly thought he was their keeper coming to feed them.",
            "A group of eagles is called a convocation.",
            "Baby hedgehogs are called hoglets.",
            "Male reindeer shed their antlers in winter.",
            "In Old Irish culture you could not become king without nipples.",
            "Primordial black holes have the same size as an atom but the same mass as a large mountain.",
            "In 2006 an Australian man tried to sell New Zealand on eBay.",
            "The winner of Finland's wife-carrying contest wins his wife's weight in beer.",
            "The average recovery rate for stolen art is only 2-6%.",
            "One million dogs in the US have been named as the primary beneficiary in their owners' wills.",
            "Zachary Quinto can't do the Vulcan salute, so his fingers were taped together when filming.",
            "A dentist and confectioner invented the candy floss machine.",
            "Ripe peas are yellow; we pick them before they're ripe.",
            "Albert Einstein never learned to drive.",
            "Yawning is contagious to dogs and chimps.",
            'On April 18, 1930, BBC radio reported "There is no news."',
            "There is a city in Turkey called Batman.",
            "Oklahoma's state vegetable is the watermelon.",
            "Neil Armstrong's astronaut application was a week late.",
            "10% of living Europeans were conceived on IKEA beds.",
            "The T. rex sound effect in Jurassic Park is a slowed down recording of a Jack Russell playing with a rope.",
            "'Ricotta' is the Italian word for recooked.",
            "Charlie Chaplin once lost a Charlie Chaplin lookalike contest.",
            "Bats account for a quarter of the global mammal population.",
            "Ernest Hemingway once stole a urinal from his favourite bar.",
            "In 75BC, insulted by the initial ransom demand of his pirate captors, Caesar demanded they raise the amount.",
            "Elvis Presley was naturally blond.",
            "Elephants don't like peanuts.",
            "Syrup is as easy to swim in as water, but grosser.",
            "In the early 1900s doctors treated syphilis by giving their patients malaria and curing the malaria.",
            "The world record for the most people fit into a Mini Cooper Hatchback is 28.",
            "In the 1950s Xerox machines overheated so often they came with a fire extinguisher.",
            "Bubble Wrap is a trademark.",
            "Nikola Tesla refused to speak to women wearing pearls.",
            "In the 1500s it was illegal for European physicians to treat a patient without first consulting the moon.",
            "More people live in Shanghai than in the whole of Australia.",
            "Olympic gold medals are 93% silver.",
            "Prince Charles has an Aston Martin that runs on biofuel made from wine."
            "Strawberries have more vitamin C per serving than oranges.",
            "Cyclists need 7% less oxygen when pedalling in time with music.",
            "9% of pet owners throw birthday parties for their pets.",
            "18% of Americans believe they have seen a ghost.",
            "Croquet was an Olympic sport in 1900. There was only one spectator.",
            "During the Beijing Olympics Usain Bolt ate an average of 100 McNuggets every day for ten days.",
            "You're 50 times more likely to be killed by bees than win the lottery.",
            "The French cut the lift cables in the Eiffel Tower so Hitler would have to take the stairs when he invaded.",
            "Bison vote on where to migrate next.",
            "In ancient Peru only noblewomen could brew beer.",
            "Scooby-Doo's original name was Too Much.",
            "The Macarena is about a girl who cheats on her boyfriend after he gets drafted into the military.",
            "Some cats are lactose intolerant.",
            "In the 1600s English people had accents similar to the modern-day American accent.",
            "Human eyes stop growing around the age of 13.",
            "Nikola Tesla fell in love with a pigeon, once stating 'I loved that pigeon as a man loves a woman, and she loved me'.",
            "The Scottish national animal is the unicorn.",
        ]

    @commands.command(help=LONG_HELP_TEXT, brief=SHORT_HELP_TEXT)
    async def fact(self, ctx: Context):
        display_name = get_name_string(ctx.message)
        await ctx.send(f"{display_name}: {random.choice(self.options)}")


def setup(bot: Bot):
    bot.add_cog(Fact(bot))
