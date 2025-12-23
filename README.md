# Genetic Inheritance Simulation.

## !Warning!

I am not a scientist, I am just a nerd who didn't like the existing ecosystem simulations that I have seen. I **WILL** use the wrong terms and misunderstand some parts of heredity. This is also a **significantly** simplified simulation of genetics and heredity. My plans are to increase the complexity or get closer to reality. All work here is based on my own personal research (read: web-searches, asking more well informed people) and is prone to misunderstanding and incorrect or incomplete information. Do **NOT** refer to this for education or to win an argument against your creationist aunt.

## Glossary

- **Genome** - The full and complete genetic data set.
- **Heplome** - The set of chromosomes inherited from one parent.
- **Chromosome** - A set of genes, grouped into a packet, that is can be transfered from parent to child.
- **Gene** - A single piece of genetic information that is used to influence the form of the body. (Not all are coding genes).
- **Dominance score** - A number that determines the strength of a gene and if it is dominant or recessive.

## Overview

The purpose of this project was to investigate ways to simulate genetic inheritence and expression for my larger ecosystem simulation.

## Controls

- **ESC** - Quit
- **Space** - Generate new child


## What it is doing

Essentially all this is doing it generating two seperate "animal" entities randomising their genes, then expressing them based on a "dominance score" for each. Then it generates a third animal entity with genetics based on the parent animals.

## Genetics

Each animal entity has two heplomes that combined make up the full genome. Each heplome is a list of chromosomes labled 'A' through 'F'. Each chromosome has a matching chromosme in the other heplome. These chromosomes are themselves lists containing genes which are tuples of two numbers. The first of these numbers is a floating point number between 0 and 10 which represents some genetic data. The second number is a floating point number between 0 and 1, which is that gene's dominance score. Each individual gene can be named by it's position in the overall genetic data structure in the following pattern: \<Chromosome>\<Gene> e.g:  the third gene on chromosome D in heplome two would be **D203**.

| Heplome 1     | Heplome 2     |
| ------------ | ------------ |
| ChromosomeA1 | ChromosomeA2 |
| ChromosomeB1 | ChromosomeB2 |
| ChromosomeC1 | ChromosomeC2 |
| ChromosomeD1 | ChromosomeD2 |
| ChromosomeE1 | ChromosomeE2 |
| ChromosomeF1 | ChromosomeF2 |

| ChromosomeA1  |
| ------------- |
| Gene A101     |
| Gene A102     |
| Gene A103     |
| Gene A104     |
| Gene A105     |
| Gene A106     |
| Gene A107     |
| Gene A108     |
| Gene A109     |
| Gene A110     |

**Gene A101** = (Gene Data, Dominance Score)

A full set of genetic data for these animals looks like so:
[[(4.91149880363438, 0.3909572401769219), (1.5082627466574499, 0.7306895859038731), (8.761263960973453, 0.47348939539441026), (8.910769400338184, 0.9993649325546438), (2.255861135988723, 0.1275106043082339)], [(2.060801075051364, 0.4825964564571713), (7.115498761902729, 0.2006180483696267), (5.244603811753485, 0.24667718210606449), (3.52642599272915, 0.7011732573593094), (4.3262144377086456, 0.02909662663461976)], [(1.103676394458916, 0.6076067521146743), (7.464512843493292, 0.5200423139825723), (5.497390373335863, 0.14456025425538666), (7.739792966771306, 0.8764231170096447), (4.20148177773208, 0.921111632239041)], [(5.661378440960346, 0.8844519367262407), (1.3043723222359012, 0.9453723698849241), (2.26644308454801, 0.14295476612007119), (2.7437139390902807, 0.5650844730893366), (5.646810873796282, 0.07825683705661557)], [(1.2206173608558424, 0.6383301916297954), (1.8654687556943539, 0.7362551588281945), (8.651071109733667, 0.5085724430148857), (3.2051004158782375, 0.14740221897636563), (4.669925392649172, 0.38466716168545534)], [(2.876085425493502, 0.6296260012941282), (1.0262646731854699, 0.7437382292168013), (5.560847760802966, 0.21957005376936967), (6.8623499433579855, 0.0038573637500821656), (7.7770681334791725, 0.1369177488466915)]]

It looks confusing, but it works.

## Inheritance

When a child is generated the software will itterate through both heplomes in both parents and randomly choose one chromosome from each pair to pass on to the child. The child entity will then itterate through each pair of chromosomes and select the gene that has the highest dominance score to add to the active gene pool. Finally, the child will then express those characteristics by altering it's height, width, and colour. These attributes are generated off certain genes in the active gene pool. I randomly chose which genes influenced each trait, but hard-coded those so it uses the same genes each time the simulation is run.

## Did I do it wrong?

If you have a better handle on genetics or programming, please let me know via email, submitting a issue, or a pull request. Please explain in as much detail as you can. I'm happy to learn or answer any questions (if I am able).

## License

GPL or something. I'm not really concerned with licenses for this. Credit would be nice, but just keep the warning in mind.