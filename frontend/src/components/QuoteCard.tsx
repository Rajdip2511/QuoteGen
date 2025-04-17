import React from "react";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";

interface QuoteCardProps {
  quote: string;
  isLoading: boolean;
  error: string | null;
  onRefresh: () => void;
}

export function QuoteCard({
  quote,
  isLoading,
  error,
  onRefresh,
}: QuoteCardProps) {
  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle className="text-center">Inspirational Quote</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="min-h-[100px] flex items-center justify-center">
          {isLoading ? (
            <p className="text-center text-muted-foreground">Loading...</p>
          ) : error ? (
            <p className="text-center text-red-500">{error}</p>
          ) : (
            <p className="text-center text-lg italic">&ldquo;{quote}&rdquo;</p>
          )}
        </div>
      </CardContent>
      <CardFooter className="flex justify-center">
        <Button
          onClick={onRefresh}
          disabled={isLoading}
          className="w-full max-w-[200px]"
        >
          {isLoading ? "Loading..." : "New Quote"}
        </Button>
      </CardFooter>
    </Card>
  );
} 