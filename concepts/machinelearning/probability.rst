This process of “inferring” insights from sample data is called “Inferential Statistics”.
random variable X basically converts outcomes of experiments to something measurable.
it is used for numerical formulation of a random process

probability  = Favourable outcomes / Total outcomes
probability distribution is ANY form of representation that tells us the probability for all possible values of X.

The binomial distribution gives us the expected number of successes (drawing a red ball) in 
n trials (where n is the number of players). 
The expected number  E(X) is given by: E(X)=n⋅p

if X can take x1, x2, x3 .... xn
Expected Value : x1 *(P(X = x1)) + x2 *(P(X = x2)) + x3 *(P(X = x3)) ..... + xn *(P(X = xn))
P(X = xi) denotes the probability that X is equal to xi
It is also called the expectation, average, and mean value.
it is average value of random variable if the random process is repeated multiple times

sum of all probability will always be 1.

The expected value should be interpreted as the average value you get after the experiment has been conducted an infinite number of times. For example, the expected value for the number of red balls is 2.385. This means that if we conduct the experiment (play the game) infinite times, the average number of red balls per game would end up being 2.385. 

Normal distribution
Bell shape curve

z confidence level
99% 2.58
95% 1.96
90% 1.65

To calculate the expected value of the net winnings 
𝑋
X when betting £100 on the number 5 in an American Roulette game, we need to consider the different probabilities and outcomes.

In American Roulette:

There are 38 pockets on the wheel (numbers 1-36, 0, and 00).
If you win by betting on a single number, the payout is 35 to 1. This means if you bet £100 and win, you receive your original £100 plus £3500 (35 times £100), totaling £3600.
If you lose, you lose your £100 bet.
Let's denote:

𝑃(win) = 1 / 38
𝑃(lose) = 37 / 38

X can be:

£3500 if you win (since the net winnings exclude the initial £100 bet, it would be £3600 total winnings minus the £100 bet).
-£100 if you lose (since you lose your bet).
The expected value 
𝐸
(
𝑋
)
E(X) is calculated as follows:

𝐸
(
𝑋
)
=
(
3500
×
𝑃
(
win
)
)
+
(
−
100
×
𝑃
(
lose
)
)
E(X)=(3500×P(win))+(−100×P(lose))

Substituting the probabilities:

𝐸
(
𝑋
)
=
3500
×
1
38
+
(
−
100
)
×
37
38
E(X)=3500× 
38
1
​
 +(−100)× 
38
37
​
 

𝐸
(
𝑋
)
=
3500
38
+
−
3700
38
E(X)= 
38
3500
​
 + 
38
−3700
​
 

𝐸
(
𝑋
)
=
3500
−
3700
38
E(X)= 
38
3500−3700
​
 

𝐸
(
𝑋
)
=
−
200
38
E(X)= 
38
−200
​
 

𝐸
(
𝑋
)
=
−
100
19
≈
−
5.26
E(X)=− 
19
100
​
 ≈−5.26

Therefore, the expected value of 
𝑋
X, the net winnings when betting £100 on the number 5 in an American Roulette game, is approximately 
−
£
5.26
−£5.26. This negative expected value reflects the house edge in American Roulette.

Expected Value = (win Value * P(win)) + (lose Value * P(lose))

multiplication rule of probability 
P(Event 1 and Event 2) = P(Event 1) * P(Event 2) if event 1 and event 2 are happening at same time and independent of each other

Addition rule of probability
P(Event 1 or Event 2) = P(Event 1) + P(Event 2) if event 1 or event 2 are happening at time and mutually exclusive of each other

So, the formula for finding binomial probability is given by -
P(X=r) = nCr (p)
r
(
1
−
p
)
n
−
r

 

Where n is no. of trials, p is probability of success and r is no. of successes after n trials.

the formula for finding binomial probability is given by -

P(X=r) = nCr(p)^r(1−p)^(n−r)

Where n is no. of trials, p is probability of success and r is no. of successes after n trials.

However, as Prof. Tricha said, there are some conditions that need to be followed in order for us to be able to apply the formula.

Total number of trials is fixed at n

Each trial is binary, i.e., has only two possible outcomes - success or failure

Probability of success is same in all trials, denoted by p

the cumulative probability of X, denoted by F(x), is defined as the probability of the variable being less than or equal to x.
P(60 <= X <= 65) = P(X <= 65>) - P(X <= 60)
cumulative probability F(x) = P(X<x)

continuous probability
CDF is and what a PDF is. Since these two functions talk about probabilities in terms of intervals rather than exact values, it is advisable to use them when talking about continuous random variables, and not the bar chart distribution that we used for discrete variables.
a CDF, or a cumulative distribution function, is a distribution which plots the cumulative probability of X against X.
A PDF, or Probability Density Function, however, is a function in which the area under the curve, gives you the cumulative probability.

The main difference between the cumulative probability distribution of a continuous random variable and a discrete one, is the way you plot them. While the continuous variables’ cumulative distribution is a curve, the distribution for discrete variables looks more like a bar chart:

The reason for showing both of these so differently is that, for discrete variables, the cumulative probability does not change very frequently. 

A commonly observed type of distribution among continuous variables is the uniform distribution.
For a continuous random variable following a uniform distribution, the value of probability density is equal for all possible values.

PDFs are more commonly used in real life. The reason is that it is much easier to see patterns in PDFs as compared to CDFs. 
since X is a continuous variable, you know that the probability of getting an exact value is zero. 
Hence, P(X=175.3 cm) = 0, which means that P(X ≤ 175.3 cm = P(X < 175.3 cm) + 0.

All data that is normally distributed follows the 1-2-3 rule. This rule states that there is a -
68% probability of the variable lying within 1 standard deviation of the mean
95% probability of the variable lying within 2 standard deviations of the mean
99.7% probability of the variable lying within 3 standard deviations of the mean

If the variable is normally distributed, then it doesn’t matter what the value of µ and σ is, there is a 34% probability that X lies between µ and µ + σ, i.e. P(µ < X < µ + σ = 34%). Similarly, there is a 50% probability that X is less than µ, i.e. P(X < µ = 50%). Again, this would happen regardless of what the value of µ and σ is. Hence, you can say that P(X < µ + σ) = 84% for every normal variable, no matter what the value of µ and σ is.

standardised random variable is an important parameter. It is given by:
Z=X−μ/σ
Basically, it tells you how many standard deviations away from the mean your random variable is.

P(-2 < Z < 2 ) = P(mu - 2sigma < X < mu + 2sigma) = 95% as per rule 2 from (1-2-3 rule)

P(-2<Z<3) = P(mu -2sigma < X < mu + 3sigma) = 47.5 + 49.85 =  97.35%
P(Z < 1) = P(X < mu + sigma) = 84%
P(25.2 < X < 44.8) = P(-1.96 < Z < 1.96) = P(Z = 1.96) - P(Z = -1.96) = 0.975 - 0.025 = 0.95

What is the probability of a normally distributed random variable lying within 1.65 standard deviations of the mean?
You have to find the probability of the variable lying between μ-1.65σ and μ+1.65σ. i.e. P(μ-1.65σ < X < μ+1.65σ). In terms of Z, this becomes P(-1.65 < Z < +1.65). This would be equal to P(1.65) - P(-1.65) = 0.95 - 0.05 = 0.90.

A low value of σ means that the graph is narrow, while a high value implies that the graph is wider. This will happen because the wider graph will clearly have more values away from the mean, resulting in a high standard deviation.

What is the probability that the tablet selected by QC has a paracetamol level above 450 mg?
Let’s define X as the amount of paracetamol in the selected tablet. Now, X is a normally distributed random variable, with mean μ = 510 mg and standard deviation σ = 20 mg. Now, you have to find the probability of X being more than 450, i.e. P(X>450). Converting this to Z, you get P(X>450) = P(Z>{450-510}/20) = P(Z>-3) = 1 - P(Z<-3) = 0.9987, or 99.87%.

Now, let’s say that QC decides to sample one more tablet. This time, it selects a tablet from Batch Y4. Based on previous knowledge, you know that Batch Y4 has a mean paracetamol level of 505 mg, and its standard deviation is 25 mg. This time, QC wants to check both the upper limit and the lower limit for the paracetamol level.

What is the probability that the tablet selected by QC has a paracetamol level between 450 mg and 550 mg?
Let’s define X as the amount of paracetamol in the selected tablet. Now, X is a normally distributed random variable, with mean μ = 505 mg and standard deviation σ = 25 mg. Now, you have to find the probability of X being more than 450 and less than 550, i.e. P(450 < X < 550). Converting this to Z, you get P(450 < X < 550) = P({450-505}/25 < Z < {550-505}/25) = P(-2.2 < Z < 1.8) = P(Z < 1.8) - P(Z < -2.2) = 0.9641 - 0.0139 = 0.9502, or 95%.
