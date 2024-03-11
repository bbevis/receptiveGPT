library(tidyverse)
library(qualtRics)
library(lme4)
library(lmerTest)
library(psych)
library(estimatr)
library(politeness)
library(dplyr)

raw = read.csv('gpt_outputs.csv')

recept_dat = raw %>%
  mutate(recept_baseline = politeness::receptiveness(suggestions_baselines),
         recept_recipe = politeness::receptiveness(suggestions_recipe),
         recept_words = politeness::receptiveness(suggestions_words))

recept_dat %>%
  select(recept_baseline, recept_recipe, recept_words) %>%
  colMeans()


