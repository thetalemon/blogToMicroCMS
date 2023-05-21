import { client, POST_LIST_ENDPOINT } from '../../libs/client'
import type { Post } from '../../type/post'
import styles from '../../styles/article.module.scss'
import { format } from 'date-fns'

type StaticParams = {
  params: {
    id: string
  }
}

export const generateStaticParams = async () => {
  const data = await client.get({ endpoint: POST_LIST_ENDPOINT })
  const postList = data.contents as Post[]
  const paths = postList?.map(({ id }) => ({
    id,
  }))
  return paths
}

export const getPost = async (id: string): Promise<Post> => {
  const data = await client.get({
    endpoint: POST_LIST_ENDPOINT,
    contentId: id,
  })
  return data
}

export const Page = async ({ params: { id } }: StaticParams) => {
  const post = await getPost(id)
  return (
    <main className={styles.main}>
      <div className={styles.inner}>
        <h1 className={styles.title}>{post.title}</h1>
        <p className={styles.categoryList}>
          {post.category.map((category) => (
            <span key={category.id} className={styles.category}>
              {category.name}
            </span>
          ))}
        </p>
        <p className={styles.publishedAt}>
          {format(
            new Date(post.importData.publishDate ?? post.publishedAt),
            'yyyy/MM/dd HH:mm'
          )}
        </p>
        <div
          dangerouslySetInnerHTML={{
            __html: `${post.importData.content ?? post.content}`,
          }}
          className={styles.post}
        />
      </div>
    </main>
  )
}

export default Page
