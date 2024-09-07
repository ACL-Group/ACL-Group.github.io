@Model
class SLDA(K: Long, V: Long, alpha: Double, beta: Double) {
  val phi = for (i <- 0L until K) yield Dirichlet(beta, V)
  val theta = for (i <- ?) yield Dirichlet(alpha, K)
  val z = theta.map{theta => for (i <- ?) yield Categorical(theta)}
  val x = z.map(_.map(z => ?.map(_ => Categorical(phi(z)))))
}
