import { Heading, Container, Stack, Link, Text } from '@chakra-ui/react';
import { getNews } from '../../lib/api';

export const revalidate = 900; // 15m para noticias

export default async function NewsPage() {
  const data = await getNews();
  const news = data?.results || [];
  return (
    <Container maxW="5xl" py={10}>
      <Heading mb={6}>Noticias</Heading>
      <Stack spacing={4}>
        {news.length === 0 && <Text>Sin noticias aún.</Text>}
        {news.map((n: any) => (
          <Stack key={n.id} spacing={1} borderWidth='1px' rounded='md' p={4}>
            <Link href={n.url} target="_blank" rel="noopener noreferrer" color='blue.600' fontWeight='semibold'>{n.title}</Link>
            <Text fontSize='sm' color='gray.600'>{n.published_at}</Text>
          </Stack>
        ))}
      </Stack>
    </Container>
  );
}