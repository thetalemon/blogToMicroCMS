import './globals.scss'
import { Inter } from 'next/font/google'
import Link from 'next/link'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'blog to microCMS sample',
  description: 'ブログからmicroCMSに移行するサンプル',
  robots: 'noindex,nofollow',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang='ja'>
      <body className={inter.className}>
        <header>
          <Link href={'/'}>Blog to MicroCMS Sample</Link>
        </header>
        {children}
        <footer>
          <Link href={'https://manasas.dev/'} rel='me' target='_blank'>
            © 2023 manasas
          </Link>
        </footer>
      </body>
    </html>
  )
}
