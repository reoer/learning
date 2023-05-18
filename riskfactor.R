library(TwoSampleMR)
library(readxl)
setwd("F:\\data\\exposure")

risk <- read_excel("data.xlsx",sheet=2)
test_cancer <- read_excel("data.xlsx",sheet=1)

col2 <- test_cancer[, 1]
cancer=paste(col2[1,1])

col1 <- risk[, 1]
for(i in col1){
	exposure_risk=paste(i)
	exposure_dat <-extract_instruments(exposure_risk,p1=5e-8)
	outcome_dat <-extract_outcome_data(snps=exposure_dat$SNP, outcomes=cancer)

	dat <- harmonise_data(
   		exposure_dat = exposure_dat,
   		outcome_dat = outcome_dat)

	res <- mr(dat)

	write.table(res, file = "outcomes.csv", append = TRUE, sep = ",")
}
