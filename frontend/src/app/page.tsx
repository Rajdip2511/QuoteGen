"use client";

import { useState, useEffect } from "react";
import axios from "axios";
import { QuoteCard } from "@/components/QuoteCard";

export default function Home() {
  const [quote, setQuote] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchQuote = async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/quote`);
      setQuote(response.data.quote);
    } catch (err) {
      console.error("Error fetching quote:", err);
      setError("Failed to fetch quote. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  // Fetch quote on initial load
  useEffect(() => {
    fetchQuote();
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-4 md:p-24">
      <h1 className="text-3xl font-bold mb-8">Random Quote Generator</h1>
      <QuoteCard
        quote={quote}
        isLoading={isLoading}
        error={error}
        onRefresh={fetchQuote}
      />
    </main>
  );
} 