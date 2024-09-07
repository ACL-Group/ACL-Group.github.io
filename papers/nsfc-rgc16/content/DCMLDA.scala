@Model 
class DCMLDA(K: Long, V: Long, alpha: Double, beta: Double) {
    val doc = for (i <- ?) yield {
        val phi = (0L until K).map(_ => Dirichlet(beta, V))
        val theta = Dirichlet(alpha, K)
        val z = ?.map(_ => Categorical(theta))
        val x = z.map(z => Categorical(phi(z)))
    }
}
