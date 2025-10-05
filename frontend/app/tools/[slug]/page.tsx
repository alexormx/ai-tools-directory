import { notFound } from 'next/navigation';
import { getToolSlugs, getToolDetail } from '../../../lib/api';
import { Heading, Container, Text, Badge, Stack } from '@chakra-ui/react';

export const revalidate = 3600;

export async function generateStaticParams() {
  try {
    const slugs = await getToolSlugs();
    // Si está vacío o backend inaccesible, retorna lista vacía para evitar error en build
    return (slugs || []).map(slug => ({ slug }));
  } catch {
    return [];
  }
}

export default async function ToolDetail({ params }: { params: { slug: string } }) {
  const tool = await getToolDetail(params.slug);
  if (!tool) return notFound();
  return (
    <Container maxW="4xl" py={12}>
      <Heading mb={4}>{tool.name}</Heading>
      <Stack direction="row" spacing={2} mb={4}>
        {tool.categories?.map((c: any) => <Badge key={c.slug} colorScheme='blue'>{c.name}</Badge>)}
      </Stack>
      <Text>{tool.description || 'Sin descripción.'}</Text>
    </Container>
  );
}