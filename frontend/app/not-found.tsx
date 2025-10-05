"use client";
import { Container, Heading, Text, Button } from '@chakra-ui/react';
import Link from 'next/link';

export default function NotFound() {
  return (
    <Container maxW="lg" py={24} textAlign="center">
      <Heading mb={4} size="lg">Página no encontrada</Heading>
      <Text mb={6}>La ruta solicitada no existe o el recurso fue movido.</Text>
      <Button as={Link} href="/" colorScheme="blue">Volver al inicio</Button>
    </Container>
  );
}