import { Heading, Container, SimpleGrid, Text } from '@chakra-ui/react';
import ToolCard from '../../components/ToolCard';
import { getTools } from '../../lib/api';

export const revalidate = 3600; // ISR 1h

export default async function ToolsPage() {
  const data = await getTools();
  const tools = data?.results || [];
  return (
    <Container maxW="6xl" py={10}>
      <Heading mb={6}>Herramientas</Heading>
      {tools.length === 0 && <Text>Sin datos (placeholder mientras el backend se implementa).</Text>}
      <SimpleGrid columns={{ base: 1, sm: 2, md: 3 }} spacing={6}>
        {tools.map((t: any) => <ToolCard key={t.slug} tool={t} />)}
      </SimpleGrid>
    </Container>
  );
}