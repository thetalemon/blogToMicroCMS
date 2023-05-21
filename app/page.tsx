import Link from 'next/link'
import { client, POST_LIST_ENDPOINT } from './libs/client'
import type { Post } from './type/post'
import styles from './styles/index.module.scss'

export const getPosts = async (): Promise<Post[]> => {
  const data = await client.get({ endpoint: POST_LIST_ENDPOINT })

  return data.contents as Post[]
}

export const Home = async () => {
  const postList = await getPosts()

  return (
    <main className={styles.main}>
      <h1>Blog to MicroCMS Sample</h1>
      <p className={styles.description}>
        ブログ（MT形式）からMicroCMSに移行するサンプルとして作成したもの。
        解説は<Link href={`/`}>コチラ</Link>。
      </p>

      <hr />
      <ul className={styles.list}>
        {postList.map((post: Post) => (
          <li key={post.id}>
            <Link href={`/article/${post.id}`}>{post.title}</Link>
          </li>
        ))}
      </ul>
    </main>
  )
}

export default Home
