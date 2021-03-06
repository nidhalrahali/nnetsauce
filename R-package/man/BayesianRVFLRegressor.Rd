% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/rvfl.R
\name{BayesianRVFLRegressor}
\alias{BayesianRVFLRegressor}
\title{Bayesian Random Vector Functional link network with 1 shrinkage parameter}
\usage{
BayesianRVFLRegressor(
  n_hidden_features = 5L,
  activation_name = "relu",
  a = 0.01,
  nodes_sim = "sobol",
  bias = TRUE,
  dropout = 0,
  direct_link = TRUE,
  n_clusters = 2L,
  cluster_encode = TRUE,
  type_clust = "kmeans",
  col_sample = 1,
  row_sample = 1,
  s = 0.1,
  sigma = 0.05,
  seed = 123L,
  backend = c("cpu", "gpu", "tpu")
)
}
\arguments{
\item{backend}{}
}
\value{

}
\description{
Bayesian Random Vector Functional link network with 1 shrinkage parameter
}
\examples{

set.seed(123)
n <- 50 ; p <- 3
X <- matrix(rnorm(n * p), n, p) # no intercept!
y <- rnorm(n)

obj <- BayesianRVFLRegressor(n_hidden_features = 5L)
print(obj$fit(X, y))
print(obj$score(X, y))

}
