import { Heading, Text, Container, Stack, Button } from '@chakra-ui/react';
import Link from 'next/link';

export default function HomePage() {
  return (
    <Container maxW="5xl" py={16}>
      <Stack spacing={6}>
        <Heading as="h1" size="xl">AI Tools Directory</Heading>
        <Text fontSize="lg">Explora, analiza y mantente al día con las mejores herramientas de Inteligencia Artificial.</Text>
        <Stack direction="row" spacing={4}>
          <Button as={Link} href="/tools" colorScheme="blue">Ver Herramientas</Button>
          <Button as={Link} href="/news" variant="outline">Noticias</Button>
        </Stack>
      </Stack>
    </Container>
  );
}